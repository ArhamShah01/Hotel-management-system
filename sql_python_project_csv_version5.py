#HELLO

import mysql.connector
import pandas as pd
import os
import time
import random

# CSV file path
csv_path = r"C:\Users\arham\Downloads\python sql project\customer_data_unique.csv"

# Database connection
db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')

mycursor = db.cursor()

# Drop existing tables to start fresh
mycursor.execute("DROP TABLE IF EXISTS hoteldata")
mycursor.execute("DROP TABLE IF EXISTS Room")
mycursor.execute("DROP TABLE IF EXISTS Customer")
db.commit()

# Create fresh tables
mycursor.execute("""create table if not exists hoteldata(Ccode int(5) primary key,Cname varchar(20),Cadd varchar(20),Cindate varchar(15),Coutdate nvarchar(15),Room_no varchar(5), Room_rent varchar(10),Food_bill varchar(10) default '00',Laudry_bill varchar(10) default'00',Game_bill varchar(10) default '00',SubTotal_bill varchar(10),Add_charges nvarchar(10) default '1800',GrandTotal_bill varchar(10))""")

mycursor.execute("""create table if not exists Room(Rooms varchar(10),Type nvarchar(45),Charges int(7),Features varchar(90),Occupancy int(45))""")

mycursor.execute("""insert into Room values('1-500','Duplex',6000,'Two rooms onsame floor connected by common stairs',5)""")

mycursor.execute("""insert into Room values('501-1000','Cabana',5000,'Faces waterbody,beach or a swimming pool',3)""")

mycursor.execute("""insert into Room values('1001-1500','Lanai',4000,'This room faces a landscape, a waterfall, or a garden',4)""")

mycursor.execute("""insert into Room values('1501-2000','Suit',3000, 'It is composed ofone or more bedrooms, a living room, and a dining area',12)""")

mycursor.execute("""create table if not exists Customer(Ccode varchar(10),Cname nvarchar(50),Cid_type nvarchar(20),Cid_no varchar(25) primary key , Cadd varchar(50),CNationality varchar(20),Cindate varchar(15),Coutdate varchar(15),Room_no varchar(5), Ccontact_no varchar(15))""")

db.commit()

# Import customer data from CSV
print("Importing customer data from CSV...")
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path, header=None)
    
    # CSV columns: Ccode(0), Cname(1), Cid_type(2), Cid_no(3), Cadd(4), CNationality(5), Cindate(6), Coutdate(7), Room_no(8), Ccontact_no(9)
    for index, row in df.iterrows():
        try:
            mycursor.execute(
                """insert into Customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (str(row[0]).strip(), str(row[1]).strip(), str(row[2]).strip(), str(row[3]).strip(), 
                 str(row[4]).strip(), str(row[5]).strip(), str(row[6]).strip(), str(row[7]).strip(), 
                 str(row[8]).strip(), str(row[9]).strip())
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
            while z == 'y':
                display()
                z = input("Do you want to continue..(y/n):")
            if (z == 'n'):
                return hotelfarecal()
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
    l = 0
    p = 0
    s = 0
    verify = 0
    
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    
    mycursor = db.cursor()
    
    Ccode = input("Enter Customer Code:")
    Cname = input("Enter Customer Name:")
    Cadd = input("Enter Customer Address:")
    Cindate = input("Enter Customer Check in Date(yyyy-mm-dd):")
    Coutdate = input("Enter Customer Check out Date(yyyy-mm-dd):")
    Cid_type = input("Enter your Identity card name:")
    Cid_no = input("Enter your Identity number:")
    Ccontact_no = input("Enter your Contact number:")
    CNationality = input("Enter your nationality:")
    
    try:
        mycursor.execute("insert into Customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                        (Ccode, Cname, Cid_type, Cid_no, Cadd, CNationality, Cindate, Coutdate, '', Ccontact_no))
        db.commit()
        print("Customer record inserted successfully!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        mycursor.close()
        db.close()


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
    elif choice == '2':
        new_address = input("Enter new address: ")
        mycursor.execute("update Customer set Cadd = %s where Ccode = %s", (new_address, code))
    elif choice == '3':
        new_contact = input("Enter new contact: ")
        mycursor.execute("update Customer set Ccontact_no = %s where Ccode = %s", (new_contact, code))
    elif choice == '4':
        new_nationality = input("Enter new nationality: ")
        mycursor.execute("update Customer set CNationality = %s where Ccode = %s", (new_nationality, code))
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


if __name__ == "__main__":
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░WELCOME TO THE TAJ PALACE░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║")
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
            print("Thank you for using Hotel Management System!")
            quit()
        
        else:
            print("Wrong Choice")
