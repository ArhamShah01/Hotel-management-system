import mysql.connector
import pandas as pd
import os
import time
import random
from datetime import datetime
import csv
import string

# CSV file path
csv_path = r"customer_data_v3.csv"

# Database connection
db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')

mycursor = db.cursor()

# Drop existing tables to start fresh
mycursor.execute("DROP TABLE IF EXISTS hoteldata")
mycursor.execute("DROP TABLE IF EXISTS Room")
mycursor.execute("DROP TABLE IF EXISTS Customer")
db.commit()

# Create fresh tables
mycursor.execute("""create table if not exists hoteldata(Ccode varchar(50) primary key,Cname varchar(20),Cadd varchar(20),Cindate varchar(15),Coutdate nvarchar(15),Room_no varchar(5), Room_rent varchar(10),Food_bill varchar(10) default '00',Game_bill varchar(10) default '00',SubTotal_bill varchar(10),GrandTotal_bill varchar(10))""")

mycursor.execute("""create table if not exists Room(Rooms varchar(10),Type nvarchar(45),Charges int(7),Features varchar(90),Occupancy int(45))""")

mycursor.execute("""insert into Room values('1-500','Duplex',6000,'Two rooms onsame floor connected by common stairs',5)""")

mycursor.execute("""insert into Room values('501-1000','Cabana',5000,'Faces waterbody,beach or a swimming pool',3)""")

mycursor.execute("""insert into Room values('1001-1500','Lanai',4000,'This room faces a landscape, a waterfall, or a garden',4)""")

mycursor.execute("""insert into Room values('1501-2000','Suit',3000, 'It is composed ofone or more bedrooms, a living room, and a dining area',12)""")

mycursor.execute("""create table if not exists Customer(Ccode varchar(100),Cname nvarchar(50),Cid_type nvarchar(20),Cid_no varchar(25) primary key , Cadd varchar(50),CNationality varchar(20),Cindate varchar(15),Coutdate varchar(15),Room_no varchar(5000), Ccontact_no varchar(15), Cpurpose nvarchar(10), Csmoking nvarchar(10), Cmenu nvarchar(100), Cairport nvarchar(100), Cloyalty nvarchar(100))""")

db.commit()

# Import customer data from CSV
print("Importing customer data from CSV...")
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path, header=None)
    
    # CSV columns: Ccode(0), Cname(1), Cid_type(2), Cid_no(3), Cadd(4), CNationality(5), Cindate(6), Coutdate(7), Room_no(8), Ccontact_no(9)
    for index, row in df.iterrows():
        try:
            mycursor.execute(
                """insert into Customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (str(row[0]).strip(), str(row[1]).strip(), str(row[2]).strip(), str(row[3]).strip(), 
                 str(row[4]).strip(), str(row[5]).strip(), str(row[6]).strip(), str(row[7]).strip(), 
                 str(row[8]).strip(), str(row[9]).strip(), str(row[10]).strip(), str(row[11]).strip(),
                 str(row[12]).strip(), str(row[13]).strip(), str(row[14]).strip())
            )
        except mysql.connector.Error as e:
            print(f"Error inserting row {index}: {e}")
    
    db.commit()
    print(f"✓ Successfully imported {len(df)} customer records from CSV.\n")
else:
    print(f"CSV file not found at: {csv_path}")

def speciality():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database="HOTEL_MANAGEMENT")
    
    mycursor = db.cursor()
    
    qry = "select * from room"
    
    mycursor.execute(qry)
    
    print("DESCRIPTION:")
    
    print('''The Taj Mahal Palace, Mumbai makes a wonderful starting point from which to discover the charms that bring people from around the globe flocking to Mumbai city, India's commercial and entertainment capital. ...''')
    
    descinfo = mycursor.fetchall()
    for (Rooms, Type, Charges, Features, Occupancy) in descinfo:
        print("We have Rooms", Rooms, "of type", Type, ",it has", Features, "and occupancy of", Occupancy, "persons.")
    
    print()
    
    print("SERVICES:")
    
    print('''For the disabled, Breakfast, Restaurant, Adsl wi-fi internet, Fax, Newspapers, Transfer, Tourist information, Small animals welcome, Private parking,Guarded garage, 24h reception, 24h bar, Beaches at 500 m, Shuttle bus stop for the airport only 10 minutes away.''')
    print()
    print("FACILITIES:")
    print("ReceptionHall, Bar, Pool 10.00 a.m. – 6.00 p.m.")
    print("BOOKING:")
    print("Excursions, Guided tours, Private parties")
    print()
    
    mycursor.close()
    
    db.close()


def hotelfarecal():
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1.Booking for Room")
        print("2.Show Customer Record")
        print("3.Search Customer Record")
        print("4.Delete Customer Record")
        print("5.Update Customer Record")
        print("6.Return to Main Menu")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        b = input("Enter your choice:")
        
        if (b == '1'):
            z = 'y'
            while (z == 'y'):
                inputdata()
                z = input("Do you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("Do you want to continue..(y/n):")
        
        elif (b == '2'):
            z = 'y'
            if z == 'y':
                display()
                z = input("Do you want to continue..(y/n):")
            if z == 'y':
                hotelfarecal()
            if (z == 'n'):
                print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Thank you using Taj hotel management system░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                quit()
            else:
                print("Invalid Input!!")
                z = input("Do you want to continue..(y/n):")
        
        elif (b == '3'):
            z = 'y'
            while (z == 'y'):
                search()
                z = input("Do you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("Do you want to continue..(y/n):")
        
        elif (b == '4'):
            z = 'y'
            while (z == 'y'):
                delete()
                z = input("Do you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("Do you want to continue..(y/n):")
        
        elif (b == '5'):
            z = 'y'
            while (z == 'y'):
                update()
                z = input("Do you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
            else:
                print("Invalid Input!!")
                z = input("Do you want to continue..(y/n):")
        
        elif (b == '6'):
            break
        
        else:
            print("Invalid Input.")


def inputdata():
    global verify, Ccode, Cname, Cadd, Cindate, Coutdate, Cid_type, Cid_no, Ccontact_no, CNationality
    r = 0
    p = 0
    s = 0
    verify = 0
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    mycursor.execute("SELECT Ccode FROM customer ORDER BY Ccode DESC LIMIT 1")
    result = mycursor.fetchone()
    last_id = result[0]  # e.g. 'C0042'
    num = int(last_id[1:]) + 1
    Ccode = f"C{num:04d}"  
    print("Customer code allocated: ", Ccode)
    Cname = input("Enter Customer Name: ")
    Cadd = input("Enter Customer Address: ")
    Cindate = input("Enter Customer Check in Date(DD-MM-YYYY): ")
    Coutdate = input("Enter Customer Check out Date(DD-MM-YYYY): ")
    Cid_type = input("Enter Identity card type: ")
    Cid_no = input("Enter your Identity number: ")
    Ccontact_no = input("Enter your Contact number: ")
    CNationality = input("Enter your nationality: ")


    print("\n__________________________________________________")
    purpose = input("Enter purpose of stay (Business/Leisure), input (B/L): ").lower()
    if purpose == 'b':
        Cpurpose = "B"
        print("As a business traveler, you might be interested in our conference facilities and high-speed internet access.")
        print("You may avail conference hall services at a discounted rate.")
        print("\n For Claiming Business expenses: \n GST invoice No.: 1234567890")
    else:
        Cpurpose = "L"
        print("As a leisure traveler, you might enjoy our recreational amenities and dining options.")
    print("\n__________________________________________________")

    empty_rooms=get_empty_rooms()
    print("\n__________________________________________________")
    print("We have the following rooms for you:-")
    print("1. Duplex --- >Rs 15000 PN- --- > Room No.: ", empty_rooms[0])
    print("2. Cabana --- >Rs 12500 PN- --- > Room No.: ", empty_rooms[1])
    print("3. Lanai  --- >Rs 20000 PN- --- > Room No.: ", empty_rooms[2])
    print("4. Suit   --- >Rs 25000 PN- --- > Room No.: ", empty_rooms[3])
    print("5. Mini   --- >RS 7500 PN-  --- > Room No.: ", empty_rooms[4])
    print("__________________________________________________")
    while (1):
        x = int(input("Enter you choice:"))
        n = datetime.strptime(Coutdate, '%d-%m-%Y') - datetime.strptime(Cindate, '%d-%m-%Y')
        n = n.days
        if (x == 1):
            print("You have opted room Duplex")
            s = s + 15000 * n
            Room_no = random.randint(1, 501)
            break
        elif (x == 2):
            print("You have opted room Cabana")
            s = s + 12500 * n
            Room_no = random.randint(501, 1001)
            break
        elif (x == 3):
            print("You have opted room Lanai")
            s = s + 20000 * n
            Room_no = random.randint(1001, 1501)
            break
        elif (x == 4):
            print("You have opted room Suit")
            s = s + 25000 * n
            Room_no = random.randint(1501, 2001)
            break
        elif (x == 5):
            print("You have opted room mini")
            s = s + 7500 * n
            Room_no = random.randint(2001, 2501)
            break
        else:
            print("Please choose a room")


    Smoking = input("Would you like Smoking Room? (y/n): ").lower()
    if Smoking == 'y':
        Csmoking = "Yes"
        print("Smoking room selected.")
    else:
        Csmoking = "No"
        print("Non-Smoking room selected.")
    print("Your Room Number is:", Room_no)

    print("\nYour room rent is", s, 'RS')
    
    print("__________________________________________________")
    print("\n*****RESTAURANT MENU*****")
    print('''
1.breakfast      --- > Rs599
2.lunch          --- > Rs799
3.dinner         --- > Rs999
4.All meal combo --- > Rs1999 
5.Next''')
    print("__________________________________________________")
    while (1):
        c = int(input("Enter your choice:"))
        if (c == 1):
            Cmenu = "Breakfast"
            d = int(input("Enter number of people: "))
            r = r + 599 * d
            break
        elif (c == 2):
            Cmenu = "Lunch"
            d = int(input("Enter number of people: "))
            r = r + 799 * d
            break
        elif (c == 3):
            Cmenu = "Dinner"
            d = int(input("Enter number of people: "))
            r = r + 999 * d
            break
        elif (c == 4):
            Cmenu = "All meals"
            d = int(input("Enter number of people: "))
            r = r + 1999 * d
            break
        elif (c == 5):
            Cmenu = "None"
            break
        else:
            print("Invalid option")
    print ("\nTotal food Cost=Rs ", r)
    print("__________________________________________________")
    print("\n*****Airport Pickup & Drop*****")
    print('''
1.Pickup             --- > Rs700
2.Drop               --- > Rs700
3.Both Pickup & Drop --- > Rs1200
4.Next''')
    print("__________________________________________________")
    while (1):
        f = int(input("Enter your choice:"))
        if (f == 1):
            Cairport = "Pickup"
            r = r + 700
            break
        elif (f == 2):
            Cairport = "Drop"
            r = r + 700
            break
        elif (f == 3):
            Cairport = "Both"
            r = r + 1200
            break
        elif (f == 4):
            Cairport = "None"
            break
        else:
            print("Invalid option")
    print("\nTotal Airport Pickup & Drop Cost=Rs", r)
    print("__________________________________________________")
    print("\n******Amenities*******")
    print ('''
1.Table tennis    --- >Rs200
2.Bowling         --- >Rs300
3.Snooker         --- >Rs300
4.Video games     --- >Rs150
5.Swimming Pool   --- >Rs200,
6.Conference Hall --- >Rs500
7.Next''')
    print("__________________________________________________")
    while (1):
        g = int(input("Enter your choice:"))
        if (g == 1):
            h = int(input("No. of hours:"))
            p = p + 200 * h
        elif (g == 2):
            h = int(input("No. of hours:"))
            p = p + 300 * h
        elif (g == 3):
            h = int(input("No. of hours:"))
            p = p + 300 * h
        elif (g == 4):
            h = int(input("No. of hours:"))
            p = p + 150 * h
        elif (g == 5):
            h = int(input("No. of hours:"))
            p = p + 200 * h
        elif (g == 6):
            h = int(input("No. of hours:"))
            p = p + 500 * h
        elif (g == 7):
            break
        else:
            print("Invalid option")
    print("Total Game Bill=Rs", p)
    print("__________________________________________________")
    print("\n Loyalty Customer Discount: 10% on Room Rent")
    loyalty = input("Are you a loyalty customer? (y/n): ").lower()
    discount = 0
    if loyalty == 'y':
        Cloyalty = "Yes"
        discount = 0.10 * s
        loyaltycode_id = input("Please enter your loyalty code ID: ")
        print("Loyalty code verified.")
        print(f"\nYou have received a discount of Rs {discount} on your room rent.")
    else:
        Cloyalty = "No"
        print("Would you like to enroll in our loyalty program for future discounts?")
        print('Benefits include 10% off on room rent, exclusive offers, and more!')
        print("Enroll now to start saving on your next stay.")
        print("Joining is quick, easy and free of cost!")
        loyalty_input = input("Enter 'y' to enroll or 'n' to skip: ").lower()
        if loyalty_input == 'y':
            print("Thank you for enrolling in our loyalty program!")
            print_random_letters_numbers()
            
            discount = 0.10 * s
            print(f"\nYou have received a discount of Rs {discount} on your room rent.")
        else:
            print("No worries! You can enroll anytime in the future.")
    writecsv(Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality, Cindate, Coutdate, Room_no, Ccontact_no, Cpurpose, Csmoking, Cmenu, Cairport, Cloyalty)
    print("\n*******FINAL BILL*******")
    SubTotal_bill = s + r + p
    Room_rent = s
    Game_bill = p
    Food_bill = r
    GrandTotal_bill = SubTotal_bill + 0.05 * SubTotal_bill - discount
    Tax=0.05*(SubTotal_bill-discount)
    print(f"Subtotal bill is ₹ {SubTotal_bill:.2f}")
    print(f"Discount is Rs {discount:.2f}")
    print(f"Tax @5% is Rs {Tax:.2f}")
    print(f"You have to pay Rs {GrandTotal_bill:.2f}")
    print("__________________________________________________")
    rec = "insert into hoteldata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cotm = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data1 = (Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality, Cindate, Coutdate, Room_no, Ccontact_no, Cpurpose, Csmoking, Cmenu, Cairport, Cloyalty)
    data2 = (Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,Room_rent,Food_bill,Game_bill,SubTotal_bill,GrandTotal_bill)
    mycursor.execute(cotm, data1)
    mycursor.execute(rec, data2)
    db.commit()
    mycursor.close()
    print("Record Inserted ......")
    db.close()

def print_random_letters_numbers():
    letters = ''.join(random.choices(string.ascii_letters, k=4))
    numbers = ''.join(random.choices(string.digits, k=6))
    print(f"Your Loyalty Membership ID is: ", letters + numbers)



def display():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    
    mycursor = db.cursor()
    
    mycursor.execute("select * from Customer")
    
    result = mycursor.fetchall()
    
    print("\n")
    print("Customer Records:")
    print("-" * 150)
    print(f"{'Code':<10} {'Name':<20} {'ID Type':<12} {'ID No':<20} {'Address':<25} {'Nationality':<15} {'Check-in':<12} {'Check-out':<12} {'Room':<8} {'Contact':<15}")
    print("-" * 150)
    
    for record in result:
        # Safely access all 10 database fields
        try:
            ccode = record[0] if len(record) > 0 else ""
            cname = record[1] if len(record) > 1 else ""
            cid_type = record[2] if len(record) > 2 else ""
            cid_no = record[3] if len(record) > 3 else ""
            cadd = record[4] if len(record) > 4 else ""
            cnationality = record[5] if len(record) > 5 else ""
            cindate = record[6] if len(record) > 6 else ""
            coutdate = record[7] if len(record) > 7 else ""
            room_no = record[8] if len(record) > 8 else ""
            ccontact = record[9] if len(record) > 9 else ""
            
            print(f"{str(ccode):<10} {str(cname):<20} {str(cid_type):<12} {str(cid_no):<20} {str(cadd):<25} {str(cnationality):<15} {str(cindate):<12} {str(coutdate):<12} {str(room_no):<8} {str(ccontact):<15}")
        except IndexError as e:
            print(f"Error printing record {record}: {e}")
    
    print("-" * 150)
    print(f"Total records: {len(result)}")
    
    mycursor.close()
    db.close()


def search():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    
    mycursor = db.cursor()
    
    code = input("Enter Customer Code to search:")
    
    mycursor.execute("select * from Customer where Ccode = %s", (code,))
    
    result = mycursor.fetchone()
    
    if result:
        print("\nCustomer Found:")
        print(f"Code: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"ID Type: {result[2]}")
        print(f"ID Number: {result[3]}")
        print(f"Address: {result[4]}")
        print(f"Nationality: {result[5]}")
        print(f"Check-in Date: {result[6]}")
        print(f"Check-out Date: {result[7]}")
        print(f"Room: {result[8]}")
        print(f"Contact: {result[9]}")
    else:
        print("Customer not found!")
    
    mycursor.close()
    db.close()


def delete():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    
    mycursor = db.cursor()
    
    code = input("Enter Customer Code to delete:")
    
    try:
        mycursor.execute("delete from Customer where Ccode = %s", (code,))
        db.commit()
        with open('customer_data_v3.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i in range(len(rows)):
              if not rows[i] or len(rows[i]) == 0:
                continue
              if rows[i][0] == code:
                del rows[i]
                break

        with open('customer_data_v3.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        if mycursor.rowcount > 0:
            print(f"Customer record with code {code} deleted successfully!")
        else:
            print("No customer found with that code!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        mycursor.close()
        db.close()


def update():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    
    mycursor = db.cursor()
    
    code = input("Enter Customer Code to update:")
    
    print("What do you want to update?")
    print("1. Name")
    print("2. Address")
    print("3. Contact Number")
    print("4. Nationality")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        new_name = input("Enter new name: ")
        mycursor.execute("update Customer set Cname = %s where Ccode = %s", (new_name, code))
        with open('customer_data_v3.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i in range(len(rows)):
              if not rows[i] or len(rows[i]) == 0:
                continue
              if rows[i][0] == code:
                rows[i][1] = new_name
                break
        with open('customer_data_v3.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    elif choice == '2':
        new_address = input("Enter new address: ")
        mycursor.execute("update Customer set Cadd = %s where Ccode = %s", (new_address, code))
        with open('customer_data_v3.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i in range(len(rows)):
              if not rows[i] or len(rows[i]) == 0:
                continue
              if rows[i][0] == code:
                rows[i][4] = new_address
                break
        with open('customer_data_v3.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    elif choice == '3':
        new_contact = input("Enter new contact: ")
        mycursor.execute("update Customer set Ccontact_no = %s where Ccode = %s", (new_contact, code))
        with open('customer_data_v3.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i in range(len(rows)):
              if not rows[i] or len(rows[i]) == 0:
                continue
              if rows[i][0] == code:
                rows[i][9] = new_contact
                break
        with open('customer_data_v3.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    elif choice == '4':
        new_nationality = input("Enter new nationality: ")
        mycursor.execute("update Customer set CNationality = %s where Ccode = %s", (new_nationality, code))
        with open('customer_data_v3.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i in range(len(rows)):
              if not rows[i] or len(rows[i]) == 0:
                continue
              if rows[i][0] == code:
                rows[i][5] = new_nationality
                break
        with open('customer_data_v3.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    else:
        print("Invalid choice!")
    
    try:
        db.commit()
        if mycursor.rowcount > 0:
            print("Record updated successfully!")
        else:
            print("No customer found with that code!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        mycursor.close()
        db.close()

def get_empty_rooms():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    cursor = db.cursor()

    # Define the ranges
    ranges = [
        (1, 500),
        (501, 1000),
        (1001, 1500),
        (1501, 2000),
        (2001, 2500)
    ]

    occupied_rooms = []
    empty_rooms=[0,0,0,0,0]
    # Loop through each range and count empty rooms
    for low, high in ranges:
        query = """
            SELECT COUNT(*) 
            FROM customer 
            WHERE Room_no BETWEEN %s AND %s;
        """
        cursor.execute(query, (low, high))
        count = cursor.fetchone()[0]
        occupied_rooms.append(count)
    for i in range(5):
        empty_rooms[i]=500-occupied_rooms[i]
    return empty_rooms
    
    db.close()

def writecsv(Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality, Cindate, Coutdate, Room_no, Ccontact_no, Cpurpose, Csmoking, Cmenu, Cairport, Cloyalty):

    data = [Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality, Cindate, Coutdate, Room_no, Ccontact_no, Cpurpose, Csmoking, Cmenu, Cairport, Cloyalty]

    with open('customer_data_v3.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Data appended to Database successfully.")

if __name__ == "__main__":
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░WELCOME TO THE TAJ PALACE░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    
    print("\nHello Customer!")
    curr = time.ctime()
    
    t = curr.split()
    
    htime = t[3]
    
    hour = int(htime[0:2])
    
    if hour < 12:
        print('Good Morning!')
    
    if hour >= 12 and hour < 17:
        print('Good Afternoon!')
    
    if hour >= 17:
        print('Good Evening!')
    
    print(curr)
    
    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Speciality of your Hotel")
        print("2. Customer Management")
        print("3. EXIT")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        b = input("Enter your choice: ")
        
        if (b == '1'):
            speciality()
        
        elif (b == '2'):
            hotelfarecal()
        
        elif (b == '3'):
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Thank you using Taj hotel management system░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
            quit()
        
        else:

            print("Wrong Choice")

