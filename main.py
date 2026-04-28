import mysql.connector
import pandas as pd
import os
import time
import random
from datetime import datetime
import csv
import string

# CSV file path
csv_path = r"customer_data.csv"

# Database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.getenv("SQL_PASSWORD"),
    database='HOTEL_MANAGEMENT'
)
mycursor = db.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS Customer(
    Ccode       VARCHAR(100),
    Cname       NVARCHAR(50),
    Cid_type    NVARCHAR(20),
    Cid_no      VARCHAR(25) PRIMARY KEY,
    Cadd        VARCHAR(50),
    CNationality VARCHAR(20),
    Cindate     VARCHAR(15),
    Coutdate    VARCHAR(15),
    Room_no     INT,
    Ccontact_no VARCHAR(20),
    Cpurpose    NVARCHAR(10),
    Csmoking    NVARCHAR(10),
    Cmenu       NVARCHAR(100),
    Cairport    NVARCHAR(100),
    Cloyalty    NVARCHAR(100)
)""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS hoteldata(
    Ccode           VARCHAR(50) PRIMARY KEY,
    Cname           VARCHAR(50),
    Cadd            VARCHAR(50),
    Cindate         VARCHAR(15),
    Coutdate        NVARCHAR(15),
    Room_no         INT,
    Room_rent       VARCHAR(10),
    Food_bill       VARCHAR(10)  DEFAULT '00',
    Game_bill       VARCHAR(10)  DEFAULT '00',
    Transport_bill  VARCHAR(20)  DEFAULT '00',
    SubTotal_bill   VARCHAR(10),
    GrandTotal_bill VARCHAR(10)
)""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS Room(
    Rooms       VARCHAR(10),
    Type        NVARCHAR(45),
    Charges     INT,
    Features    VARCHAR(90),
    Occupancy   INT
)""")

# Only seed Room data if the table is empty (idempotent on restart)
mycursor.execute("SELECT COUNT(*) FROM Room")
if mycursor.fetchone()[0] == 0:
    mycursor.execute("INSERT INTO Room VALUES('1-500',   'Duplex', 15000, 'Two rooms on same floor connected by common stairs', 5)")
    mycursor.execute("INSERT INTO Room VALUES('501-1000','Cabana', 12500, 'Faces waterbody, beach or a swimming pool', 3)")
    mycursor.execute("INSERT INTO Room VALUES('1001-1500','Lanai', 20000, 'This room faces a landscape, a waterfall, or a garden', 4)")
    mycursor.execute("INSERT INTO Room VALUES('1501-2000','Suite', 25000, 'One or more bedrooms, a living room, and a dining area', 12)")
    mycursor.execute("INSERT INTO Room VALUES('2001-2500','Mini',   7500, 'One bedroom and a living room', 2)")

db.commit()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_int_input(prompt):
    """FIX #7: Wrap int(input()) so non-numeric input raises no unhandled error."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def is_valid_csv_row(row):
    """
    FIX #9: Reject clearly invalid / test rows during CSV import.
    Checks that both dates parse correctly and room_no is an integer.
    """
    try:
        datetime.strptime(str(row[6]).strip(), '%d-%m-%Y')
        datetime.strptime(str(row[7]).strip(), '%d-%m-%Y')
        int(str(row[8]).strip())
        # Name must contain at least one letter
        if not any(c.isalpha() for c in str(row[1]).strip()):
            return False
        return True
    except (ValueError, IndexError):
        return False


print("Importing customer data from CSV...")
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path, header=None)
    imported = 0
    skipped = 0
    for index, row in df.iterrows():
        if not is_valid_csv_row(row):
            skipped += 1
            continue
        try:
            mycursor.execute(
                """INSERT IGNORE INTO Customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (str(row[0]).strip(), str(row[1]).strip(), str(row[2]).strip(),
                 str(row[3]).strip(), str(row[4]).strip(), str(row[5]).strip(),
                 str(row[6]).strip(), str(row[7]).strip(), int(str(row[8]).strip()),
                 str(row[9]).strip(), str(row[10]).strip(), str(row[11]).strip(),
                 str(row[12]).strip(), str(row[13]).strip(), str(row[14]).strip())
            )
            imported += 1
        except mysql.connector.Error as e:
            print(f"  Row {index} skipped — DB error: {e}")
    db.commit()
    print(f"✓ CSV import done: {imported} new records, {skipped} invalid rows skipped.\n")
else:
    print(f"CSV file not found at: {csv_path}")


# ---------------------------------------------------------------------------
# Core feature functions
# ---------------------------------------------------------------------------

def speciality():
    db2 = mysql.connector.connect(
        host='localhost', user='root',
        password=os.getenv("SQL_PASSWORD"), database="HOTEL_MANAGEMENT"
    )
    cur2 = db2.cursor()
    cur2.execute("SELECT * FROM Room")

    print("\nDESCRIPTION:")
    print("The Taj Mahal Palace, Mumbai makes a wonderful starting point from which "
          "to discover the charms that bring people from around the globe flocking "
          "to Mumbai city, India's commercial and entertainment capital.")

    for (Rooms, Type, Charges, Features, Occupancy) in cur2.fetchall():
        print(f"  Rooms {Rooms} — Type: {Type} | {Features} | Occupancy: {Occupancy} persons.")

    print("\nSERVICES:")
    print("Breakfast, Restaurant, ADSL Wi-Fi, Fax, Newspapers, Transfer, Tourist "
          "information, Small animals welcome, Private parking, Guarded garage, "
          "24h reception, 24h bar, Beaches at 500 m, Airport shuttle 10 min away.")
    print("\nFACILITIES: Reception Hall, Bar, Pool 10:00–18:00")
    print("BOOKING: Excursions, Guided tours, Private parties\n")

    cur2.close()
    db2.close()


def print_random_letters_numbers():
    letters = ''.join(random.choices(string.ascii_letters, k=4))
    numbers = ''.join(random.choices(string.digits, k=6))
    print(f"Your Loyalty Membership ID is: {letters}{numbers}")


def get_empty_rooms():
    """
    FIX #5 (continued): Room_no is now INT in the Customer table so the
    BETWEEN comparison here is integer-to-integer — no implicit cast needed.
    """
    db2 = mysql.connector.connect(
        host='localhost', user='root',
        password=os.getenv("SQL_PASSWORD"), database='HOTEL_MANAGEMENT'
    )
    cur2 = db2.cursor()
    ranges = [(1, 500), (501, 1000), (1001, 1500), (1501, 2000), (2001, 2500)]
    capacity = 500
    empty_rooms = []
    for low, high in ranges:
        cur2.execute(
            "SELECT COUNT(*) FROM Customer WHERE Room_no BETWEEN %s AND %s",
            (low, high)
        )
        occupied = cur2.fetchone()[0]
        empty_rooms.append(capacity - occupied)
    cur2.close()
    db2.close()
    return empty_rooms


def writecsv(Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality,
             Cindate, Coutdate, Room_no, Ccontact_no,
             Cpurpose, Csmoking, Cmenu, Cairport, Cloyalty):
    data = [Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality,
            Cindate, Coutdate, Room_no, Ccontact_no,
            Cpurpose, Csmoking, Cmenu, Cairport, Cloyalty]
    with open('customer_data_v3.csv', 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(data)
    print("Data appended to CSV backup successfully.")


def display():
    db2 = mysql.connector.connect(
        host='localhost', user='root',
        password=os.getenv("SQL_PASSWORD"), database='HOTEL_MANAGEMENT'
    )
    cur2 = db2.cursor()
    cur2.execute("SELECT * FROM Customer")
    result = cur2.fetchall()

    print("\nCustomer Records:")
    print("-" * 150)
    print(f"{'Code':<10} {'Name':<20} {'ID Type':<12} {'ID No':<25} "
          f"{'Address':<25} {'Nationality':<15} {'Check-in':<12} "
          f"{'Check-out':<12} {'Room':<8} {'Contact':<15}")
    print("-" * 150)
    for r in result:
        print(f"{str(r[0]):<10} {str(r[1]):<20} {str(r[2]):<12} {str(r[3]):<25} "
              f"{str(r[4]):<25} {str(r[5]):<15} {str(r[6]):<12} "
              f"{str(r[7]):<12} {str(r[8]):<8} {str(r[9]):<15}")
    print("-" * 150)
    print(f"Total records: {len(result)}")
    cur2.close()
    db2.close()


def search():
    db2 = mysql.connector.connect(
        host='localhost', user='root',
        password=os.getenv("SQL_PASSWORD"), database='HOTEL_MANAGEMENT'
    )
    cur2 = db2.cursor()
    code = input("Enter Customer Code to search: ")
    cur2.execute("SELECT * FROM Customer WHERE Ccode = %s", (code,))
    result = cur2.fetchone()
    if result:
        labels = ["Code", "Name", "ID Type", "ID No", "Address", "Nationality",
                  "Check-in", "Check-out", "Room", "Contact", "Purpose",
                  "Smoking", "Menu", "Airport", "Loyalty"]
        print("\nCustomer Found:")
        for label, value in zip(labels, result):
            print(f"  {label}: {value}")
    else:
        print("Customer not found.")
    cur2.close()
    db2.close()


def delete():
    db2 = mysql.connector.connect(
        host='localhost', user='root',
        password=os.getenv("SQL_PASSWORD"), database='HOTEL_MANAGEMENT'
    )
    cur2 = db2.cursor()
    code = input("Enter Customer Code to delete: ")
    try:
        cur2.execute("DELETE FROM Customer WHERE Ccode = %s", (code,))
        db2.commit()
        if cur2.rowcount > 0:
            # Mirror deletion in CSV backup
            backup = 'customer_data_v3.csv'
            if os.path.exists(backup):
                with open(backup, 'r', newline='', encoding='utf-8') as f:
                    rows = list(csv.reader(f))
                rows = [r for r in rows if not r or r[0] != code]
                with open(backup, 'w', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerows(rows)
            print(f"Customer {code} deleted successfully.")
        else:
            print("No customer found with that code.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cur2.close()
        db2.close()


def update():
    db2 = mysql.connector.connect(
        host='localhost', user='root',
        password=os.getenv("SQL_PASSWORD"), database='HOTEL_MANAGEMENT'
    )
    cur2 = db2.cursor()
    code = input("Enter Customer Code to update: ")
    print("What do you want to update?\n1. Name\n2. Address\n3. Contact Number\n4. Nationality")

    field_map = {
        '1': ('Cname',        1, "Enter new name: "),
        '2': ('Cadd',         4, "Enter new address: "),
        '3': ('Ccontact_no',  9, "Enter new contact number: "),
        '4': ('CNationality', 5, "Enter new nationality: "),
    }

    while True:
        choice = input("Enter your choice: ")
        if choice not in field_map:
            print("Invalid choice, please try again.")
            continue
        col, csv_idx, prompt = field_map[choice]
        new_value = input(prompt)
        cur2.execute(f"UPDATE Customer SET {col} = %s WHERE Ccode = %s", (new_value, code))
        try:
            db2.commit()
            if cur2.rowcount > 0:
                # Mirror update in CSV backup
                backup = 'customer_data_v3.csv'
                if os.path.exists(backup):
                    with open(backup, 'r', newline='', encoding='utf-8') as f:
                        rows = list(csv.reader(f))
                    for row in rows:
                        if row and row[0] == code:
                            row[csv_idx] = new_value
                            break
                    with open(backup, 'w', newline='', encoding='utf-8') as f:
                        csv.writer(f).writerows(rows)
                print("Record updated successfully.")
            else:
                print("No customer found with that code.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        break

    cur2.close()
    db2.close()


def inputdata():
    db2 = mysql.connector.connect(
        host='localhost', user='root',
        password=os.getenv("SQL_PASSWORD"), database='HOTEL_MANAGEMENT'
    )
    cur2 = db2.cursor()

    cur2.execute("SELECT Ccode FROM Customer ORDER BY Ccode DESC LIMIT 1")
    result = cur2.fetchone()
    if result is None:
        Ccode = "C0001"
    else:
        num = int(result[0][1:]) + 1
        Ccode = f"C{num:04d}"
    print(f"Customer code allocated: {Ccode}")

    # ---- Input validation helpers ----
    def check_alpha(prompt, err):
        while True:
            x = input(prompt)
            if x.replace(" ", "").isalpha():
                return x
            print(err)

    def check_alnum(prompt, err):
        while True:
            x = input(prompt)
            if x.replace(" ", "").isalnum():
                return x
            print(err)

    def check_digit(prompt, err):
        while True:
            x = input(prompt)
            if x.replace(" ", "").isdigit():
                return x
            print(err)

    def check_date(prompt):
        while True:
            s = input(prompt)
            try:
                datetime.strptime(s, '%d-%m-%Y')
                return s
            except ValueError:
                print("Invalid date. Use DD-MM-YYYY format.")

    def compare_date(in_date):
        while True:
            out = check_date("Enter Customer Check-out Date (DD-MM-YYYY): ")
            if datetime.strptime(out, '%d-%m-%Y') > datetime.strptime(in_date, '%d-%m-%Y'):
                return out
            print("Check-out date must be after check-in date.")

    # ---- Collect guest details ----
    Cname       = check_alpha("Enter Customer Name: ",         "Letters only.")
    Cadd        = check_alnum("Enter Customer Address: ",      "Letters and numbers only.")
    Cindate     = check_date("Enter Customer Check-in Date (DD-MM-YYYY): ")
    Coutdate    = compare_date(Cindate)
    Cid_type    = check_alpha("Enter Identity Card Type: ",    "Letters only.")
    Cid_no      = check_digit("Enter Identity Number: ",       "Digits only.")
    Ccontact_no = check_digit("Enter Contact Number: ",        "Digits only.")
    CNationality = check_alpha("Enter Nationality: ",          "Letters only.")

    # ---- Purpose ----
    while True:
        p = input("Purpose of stay — Business (B) or Leisure (L): ").upper()
        if p == 'B':
            Cpurpose = "B"
            print("Conference facilities and high-speed internet available.")
            print("GST Invoice No.: 31PSGYJ6123G4P0")
            break
        elif p == 'L':
            Cpurpose = "L"
            print("Enjoy our recreational amenities and dining options.")
            break
        else:
            print("Invalid input. Enter B or L.")

    # ---- Room selection ----
    empty_rooms = get_empty_rooms()
    print("\n__________________________________________________")
    print("Available Rooms:")
    room_opts = [
        (1, "Duplex", 15000,  1,   501,  empty_rooms[0]),
        (2, "Cabana", 12500,  501, 1001, empty_rooms[1]),
        (3, "Lanai",  20000, 1001, 1501, empty_rooms[2]),
        (4, "Suite",  25000, 1501, 2001, empty_rooms[3]),
        (5, "Mini",    7500, 2001, 2501, empty_rooms[4]),
    ]
    for opt, name, price, _, __, avail in room_opts:
        print(f"  {opt}. {name:<8} → Rs {price:>6}/night  |  Available: {avail}")
    print("__________________________________________________")

    n = (datetime.strptime(Coutdate, '%d-%m-%Y') - datetime.strptime(Cindate, '%d-%m-%Y')).days

    while True:
        x = get_int_input("Enter room choice (1-5): ")
        if 1 <= x <= 5:
            _, rname, rprice, rlo, rhi, _ = room_opts[x - 1]
            print(f"You have chosen: {rname}")
            s = rprice * n
            Room_no = random.randint(rlo, rhi - 1)
            break
        print("Please enter a number between 1 and 5.")

    # ---- Smoking preference ----
    while True:
        sm = input("Smoking room? (y/n): ").lower()
        if sm == 'y':
            Csmoking = "Yes"; break
        elif sm == 'n':
            Csmoking = "No"; break
        else:
            print("Enter y or n.")

    print(f"Your Room Number is: {Room_no}")
    print(f"Room rent for {n} night(s): Rs {s}")

    # ---- Restaurant menu ----
    print("\n**** RESTAURANT MENU ****")
    print("  1. Breakfast      — Rs 599")
    print("  2. Lunch          — Rs 799")
    print("  3. Dinner         — Rs 999")
    print("  4. All meals      — Rs 1999")
    print("  5. None / Skip")
    r = 0
    while True:
        c = get_int_input("Enter choice: ")
        meal_map = {1: ("Breakfast", 599), 2: ("Lunch", 799),
                    3: ("Dinner", 999),    4: ("All meals", 1999)}
        if c in meal_map:
            Cmenu, unit = meal_map[c]
            d = get_int_input("Number of people: ")
            r = unit * d
            break
        elif c == 5:
            Cmenu = "None"
            break
        else:
            print("Enter 1–5.")
    print(f"Total food cost: Rs {r}")

    # ---- Airport transfer ----
    print("\n**** AIRPORT PICKUP & DROP ****")
    print("  1. Pickup             — Rs 700")
    print("  2. Drop               — Rs 700")
    print("  3. Both Pickup & Drop — Rs 1200")
    print("  4. None / Skip")
    a = 0
    while True:
        f = get_int_input("Enter choice: ")
        transport_map = {1: ("Pickup", 700), 2: ("Drop", 700), 3: ("Both", 1200)}
        if f in transport_map:
            Cairport, a = transport_map[f]
            break
        elif f == 4:
            Cairport = "None"
            break
        else:
            print("Enter 1–4.")
    print(f"Total airport transfer cost: Rs {a}")

    # ---- Amenities / Games ----
    print("\n**** AMENITIES ****")
    print("  1. Table Tennis   — Rs 200/hr")
    print("  2. Bowling        — Rs 300/hr")
    print("  3. Snooker        — Rs 300/hr")
    print("  4. Video Games    — Rs 150/hr")
    print("  5. Swimming Pool  — Rs 200/hr")
    print("  6. Conference Hall— Rs 500/hr")
    print("  7. Done")
    amenity_prices = {1: 200, 2: 300, 3: 300, 4: 150, 5: 200, 6: 500}
    p = 0
    while True:
        g = get_int_input("Enter choice: ")
        if g in amenity_prices:
            h = get_int_input("Number of hours: ")
            p += amenity_prices[g] * h
        elif g == 7:
            break
        else:
            print("Enter 1–7.")
    print(f"Total amenities cost: Rs {p}")

    # ---- Loyalty ----
    print("\nLoyalty Discount: 10% off Room Rent")
    discount = 0
    loyalty_in = input("Are you a loyalty member? (y/n): ").lower()
    if loyalty_in == 'y':
        Cloyalty = "Yes"
        # NOTE: Loyalty code is accepted on trust — no DB lookup performed.
        # See README for known limitation.
        _ = input("Enter your loyalty code ID: ")
        print("Loyalty code accepted.")
        discount = 0.10 * s
        print(f"Discount applied: Rs {discount:.2f}")
    else:
        Cloyalty = "No"
        print("Enroll in our loyalty program for 10% off future stays!")
        if input("Enroll now? (y/n): ").lower() == 'y':
            print("Welcome to the loyalty program!")
            print_random_letters_numbers()
            discount = 0.10 * s
            print(f"First-stay discount applied: Rs {discount:.2f}")
        else:
            print("You can enroll anytime — just ask at the front desk.")

    # ---- Final bill ----
    SubTotal_bill  = s + r + p + a
    Tax            = 0.05 * SubTotal_bill
    GrandTotal_bill = SubTotal_bill + Tax - discount

    print("\n******* FINAL BILL *******")
    print(f"  Room Rent      : Rs {s:.2f}")
    print(f"  Food           : Rs {r:.2f}")
    print(f"  Amenities      : Rs {p:.2f}")
    print(f"  Transport      : Rs {a:.2f}")
    print(f"  Subtotal       : Rs {SubTotal_bill:.2f}")
    print(f"  Tax (5%)       : Rs {Tax:.2f}")
    print(f"  Discount       : Rs {discount:.2f}")
    print(f"  GRAND TOTAL    : Rs {GrandTotal_bill:.2f}")
    print("__________________________________________________")

    # ---- Persist to DB ----
    data_customer = (Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality,
                     Cindate, Coutdate, Room_no, Ccontact_no,
                     Cpurpose, Csmoking, Cmenu, Cairport, Cloyalty)
    data_billing  = (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no,
                     s, r, p, a, SubTotal_bill, GrandTotal_bill)

    try:
        cur2.execute(
            "INSERT INTO Customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            data_customer
        )
        cur2.execute(
            "INSERT INTO hoteldata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            data_billing
        )
        db2.commit()
        print("Record saved to database.")

        writecsv(*data_customer)

    except mysql.connector.Error as e:
        db2.rollback()
        print(f"Database error — record NOT saved: {e}")
    finally:
        cur2.close()
        db2.close()


# ---------------------------------------------------------------------------
# Menu system
# ---------------------------------------------------------------------------

def hotelfarecal():
    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Book a Room")
        print("2. Show All Customer Records")
        print("3. Search Customer Record")
        print("4. Delete Customer Record")
        print("5. Update Customer Record")
        print("6. Return to Main Menu")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        b = input("Enter your choice: ")

        if b == '1':
            while True:
                inputdata()
                if input("Book another room? (y/n): ").lower() != 'y':
                    break

        elif b == '2':
            while True:
                display()
                if input("View again? (y/n): ").lower() != 'y':
                    break

        elif b == '3':
            while True:
                search()
                if input("Search another? (y/n): ").lower() != 'y':
                    break

        elif b == '4':
            while True:
                delete()
                if input("Delete another? (y/n): ").lower() != 'y':
                    break

        elif b == '5':
            while True:
                update()
                if input("Update another? (y/n): ").lower() != 'y':
                    break

        elif b == '6':
            break

        else:
            print("Invalid option. Please enter 1–6.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    banner = "░" * 137
    print(banner)
    print("░" + " " * 47 + "WELCOME TO THE TAJ PALACE" + " " * 64 + "░")
    print(banner)

    hour = datetime.now().hour
    greeting = "Good Morning!" if hour < 12 else ("Good Afternoon!" if hour < 17 else "Good Evening!")
    print(f"\nHello, Customer!  {greeting}  —  {time.ctime()}\n")

    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Hotel Speciality")
        print("2. Customer Management")
        print("3. Exit")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        b = input("Enter your choice: ")

        if b == '1':
            speciality()
        elif b == '2':
            hotelfarecal()
        elif b == '3':
            print(banner)
            print("░" + " " * 35 + "Thank you for using Taj Hotel Management System" + " " * 53 + "░")
            print(banner)
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")
