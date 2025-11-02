import mysql.connector
import time
import random

# Database connection and table creation
db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
mycursor = db.cursor()
mycursor.execute("show tables")
tabs = mycursor.fetchall()
if (('hoteldata',) not in tabs) and (('Room',) not in tabs) and (('Customer',) not in tabs):
    mycursor.execute("""create table if not exists hoteldata(Ccode int(5) primary key,Cname varchar(20),Cadd varchar(20),Cindate varchar(15),Coutdate nvarchar(15),Room_no varchar(5), Room_rent varchar(10),Food_bill varchar(10) default '00',Laudry_bill varchar(10) default'00',Game_bill varchar(10) default '00',SubTotal_bill varchar(10),Add_charges nvarchar(10) default '1800',GrandTotal_bill varchar(10))""")
    mycursor.execute("insert into hoteldata values(25,'Deepak','Morar,Gwalior','2024-11-25','2024-11-26',1000,6000,150,10,180,6340,1800,8140)")
    mycursor.execute("insert into hoteldata values(26,'Amit','Morar,Gwalior','2024-10-05','2024-10-08',1017,10000,5,0,50,10155,1800,11955)")
    mycursor.execute("insert into hoteldata values(27,'Anuj','New Delhi','2024-07-12','2024-07-20',1407,000,130,7,80,4217,1800,6017)")
    mycursor.execute("insert into hoteldata values(28,'Kunal','Morar,Gwalior','2022-03-05','2022-03-08',1405,9000,20,0,90,9110,1800,10910)")
    mycursor.execute("insert into hoteldata values(29,'Smith','Canada','2023-11-23','2023-11-30',1008,3000,20,5,50,30075,1800,31875)")
    mycursor.execute("insert into hoteldata values(30,'Alex','America','2023-12-25','2024-01-01',1012,3000,30,6,0,30036,1800,31836)")
    mycursor.execute("""create table if not exists Room(Rooms varchar(10),Type nvarchar(45),Charges int(7),Features varchar(90),Occupancy int(45))""")
    mycursor.execute("insert into Room values('1-500','Duplex',6000,'Two rooms onsame floor connected by common stairs',5)")
    mycursor.execute("insert into Room values('501-1000','Cabana',5000,'Faces waterbody,beach or a swimming pool',3)")
    mycursor.execute("insert into Room values('1001-1500','Lanai',4000,'This room faces a landscape, a waterfall, or a garden',4)")
    mycursor.execute("insert into Room values('1501-2000','Suit',3000, 'It is composed ofone or more bedrooms, a living room, and a dining area',12)")
    mycursor.execute("""create table if not exists Customer(Ccode int(5),Cname nvarchar(15),Cadd varchar(20),Cindate varchar(15),Coutdate varchar(15),Cid_type nvarchar(20),Cid_no varchar(15) primary key , Ccontact_no varchar(15), CNationality varchar(10))""")
    mycursor.execute("insert into Customer values(25,'Deepak','Morar,Gwalior','2024-11-25','2024-11-26','Aadhaar card',412563578952,8269513294,'Indian')")
    mycursor.execute("insert into Customer values(26,'Amit','Morar,Gwalior','2024-10-05','2024-10-08','Pan card',5874695325,9063560847,'Indian')")
    mycursor.execute("insert into Customer values(27, 'Anuj','New Delhi','2024-07-12','2024-07-20','Pan card',8456958236,9770563593,'Indian')")
    mycursor.execute("insert into Customer values(28,'Kunal','Morar,Gwalior','2023-11-23','2023-11-30','Service Id',8546952156,4856985123,'Indian')")
    mycursor.execute("insert into Customer values(29,'Smith','Canada','2023-11-23','2023-11-30','Voter Id Card',45896244,6598541256,'Canadian')")
    mycursor.execute("insert into Customer values(30,'Alex','America','2023-12-25','2024-01-01','Aadhaar card',485962578545,6325489652,'American')")
    db.commit()

def speciality():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database="HOTEL_MANAGEMENT")
    mycursor = db.cursor()
    qry = "select * from room"
    mycursor.execute(qry)
    print("DESCRIPTION:")
    print('''The Taj Mahal Palace, Mumbai makes a wonderful starting point from which to discover the charms that bring people from around the globe flocking to Mumbai city, India’s commercial and entertainment capital. ...''')
    descinfo = mycursor.fetchall()
    for (Rooms, Type, Charges, Features, Occupancy) in descinfo:
        print("We have Rooms", Rooms, "of type", Type, ",it has", Features, "and occupancy of", Occupancy, "persons.")
        print()
    print("SERVICES:")
    print('''For the disabled, Breakfast, Restaurant, Adsl wi-fi internet, Fax, Newspapers, Transfer, Tourist information, Small animals welcome, Private parking,Guarded garage, 24h reception, 24h bar, Beaches at 500 m, Shuttle bus stop for the airport only 10 minutes away.''')
    print()
    print("FACILITIES:")
    print("ReceptionHall, Bar, Pool 10.00 a.m. – 6.00 p.m.n")
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
    Ccode = int(input("Enter Customer Code:"))
    Cname = input("Enter Customer Name:")
    Cadd = input("Enter Customer Address:")
    Cindate = input("Enter Customer Check in Date(yyyy-mm-dd):")
    Coutdate = input("Enter Customer Check out Date(yyyy-mm-dd):")
    Cid_type = input("Enter your Identity card name:")
    Cid_no = input("Enter your Identity number:")
    Ccontact_no = input("Enter your Contact number:")
    CNationality = input("Enter your nationality:")
    print("We have the following rooms for you:-")
    print("1. Duplex --- >Rs 6000 PN-")
    print("2. Cabana --- >Rs 5000 PN-")
    print("3. Lanai --- >Rs 4000 PN-")
    print("4. Suit --- >Rs 3000 PN-")
    print("5. Mini --- >RS 2000 PN-")
    print("6. Next")
    while (1):
        x = int(input("Enter you choice:"))
        if (x == 1):
            n = int(input("For How Many Nights Will You Stay ?:"))
            print("You have opted room Duplex")
            s = s + 6000 * n
            Room_no = random.randint(1, 501)
            print("Your Room Number is:", Room_no)
        elif (x == 2):
            n = int(input("For How Many Nights Will You Stay:"))
            print("You have opted room Cabana")
            s = s + 5000 * n
            Room_no = random.randint(501, 1001)
            print("Your Room Number is:", Room_no)
        elif (x == 3):
            n = int(input("For How Many Nights Will You Stay:"))
            print("You have opted room Lanai")
            s = s + 4000 * n
            Room_no = random.randint(1001, 1501)
            print("Your Room Number is:", Room_no)
        elif (x == 4):
            n = int(input("For How Many Nights Will You Stay:"))
            print("You have opted room Suit")
            s = s + 3000 * n
            Room_no = random.randint(1501, 2001)
            print("Your Room Number is:", Room_no)
        elif (x == 5):
            n = int(input("For How Many Nights Will You Stay:"))
            print("You have opted room Cabana")
            s = s + 5000 * n
            Room_no = random.randint(2001, 2501)
            print("Your Room Number is:", Room_no)
        elif (x == 6):
            break
        else:
            print("Please choose a room")
    print("Your room rent is", s, 'RS')
    print("\n*****RESTAURANT MENU*****")
    print('''1.water----->Rs20,
2.tea----->Rs10,
3.breakfast combo--->Rs90,
4.lunch --- >Rs110,
5.dinner -- >Rs150,
6.Next''')
    while (1):
        c = int(input("Enter your choice:"))
        if (c == 1):
            d = int(input("Enter the quantity:"))
            r = r + 20 * d
        elif (c == 2):
            d = int(input("Enter the quantity:"))
            r = r + 10 * d
        elif (c == 3):
            d = int(input("Enter the quantity:"))
            r = r + 90 * d
        elif (c == 4):
            d = int(input("Enter the quantity:"))
            r = r + 110 * d
        elif (c == 5):
            d = int(input("Enter the quantity:"))
            r = r + 150 * d
        elif (c == 6):
            break
        else:
            print("Invalid option")
    print ("\nTotal food Cost=Rs ", r)
    print("\n******LAUNDRY MENU*******")
    print ('''1.Shorts----->Rs3,
2.Trousers----->Rs4,
3.Shirt--->Rs5,
4.Jeans --- >Rs6,
5.Girlsuit -- >Rs8,
6.Next''')
    while (1):
        e = int(input("Enter your choice:"))
        if (e == 1):
            f = int(input("Enter the quantity:"))
            l = l + 3 * f
        elif (e == 2):
            f = int(input("Enter the quantity:"))
            l = l + 4 * f
        elif (e == 3):
            f = int(input("Enter the quantity:"))
            l = l + 5 * f
        elif (e == 4):
            f = int(input("Enter the quantity:"))
            l = l + 5 * f
        elif (e == 5):
            f = int(input("Enter the quantity:"))
            l = l + 6 * f
        elif (e == 6):
            break
        else:
            print("Invalid option")
    print("Total Laundary Cost=Rs", l)
    print("\n******GAME MENU*******")
    print ('''1.Table tennis----->Rs60,
2.Bowling----->Rs80,
3.Snooker--->Rs70,
4.Video games---->Rs90,
5.Pool--->Rs50==6,
6.Next''')
    while (1):
        g = int(input("Enter your choice:"))
        if (g == 1):
            h = int(input("No. of hours:"))
            p = p + 60 * h
        elif (g == 2):
            h = int(input("No. of hours:"))
            p = p + 80 * h
        elif (g == 3):
            h = int(input("No. of hours:"))
            p = p + 70 * h
        elif (g == 4):
            h = int(input("No. of hours:"))
            p = p + 90 * h
        elif (g == 5):
            h = int(input("No. of hours:"))
            p = p + 50 * h
        elif (g == 6):
            break
        else:
            print("Invalid option")
    print("Total Game Bill=Rs", p)
    SubTotal_bill = s + r + l + p
    Add_charges = 1800
    Room_rent = s
    Game_bill = p
    Food_bill = r
    Laudry_bill = l
    GrandTotal_bill = SubTotal_bill + Add_charges
    print("You have to pay Rs", GrandTotal_bill)
    rec = "insert into hoteldata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cotm = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data1 = (Ccode,Cname,Cadd,Cindate,Coutdate,Cid_type,Cid_no,Ccontact_no,CNationality)
    data2 = (Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,Room_rent,Food_bill,Laudry_bill,Game_bill,SubTotal_bill,Add_charges,GrandTotal_bill)
    mycursor.execute(cotm, data1)
    mycursor.execute(rec, data2)
    db.commit()
    mycursor.close()
    print("Record Inserted ......")
    db.close()

def display():
    print("1.Display all records")
    print("2.Display through code number")
    d = input("Enter your choice:")
    if (d == '1'):
        db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        qry = '''select h.Ccode,h.Cname,h.Cadd,h.Cindate,h.Coutdate,h.Room_no, c.CNationality, c.Ccontact_no,c.Cid_type,c.Cid_no from hoteldata h, customer c where h.Ccode=c.Ccode'''
        mycursor.execute(qry)
        for(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,CNationality,Ccontact_no,Cid_type,Cid_no) in mycursor:
            print("Customer details ......")
            print("Customer code:", Ccode)
            print("Customer name:", Cname)
            print("Customer Id type:", Cid_type)
            print("Customer Id Number:", Cid_no)
            print("Customer address:", Cadd)
            print("customer Nationality:", CNationality)
            print("Check in date:", Cindate)
            print("Check out date", Coutdate)
            print("Room number:", Room_no)
            print("Customer Contact number:", Ccontact_no)
            print("__________________________________________________")
        mycursor.close()
        print("It's All record")
        db.close()
    elif (d == '2'):
        db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = input("Enter code of customer:")
        qry = '''select h.Ccode,h.Cname,h.Cadd,h.Cindate,h.Coutdate,h.Room_no, c.CNationality,c.Ccontact_no,c.Cid_type,c.Cid_no from hoteldata h, customer c where h.Ccode=c.Ccode and h.Ccode=%s'''
        rec_code = (Ccode,)
        mycursor.execute(qry, rec_code)
        rec_count = 0
        for(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,CNationality,Ccontact_no,Cid_type,Cid_no) in mycursor:
            rec_count += 1
            print ('Record Found ..... ')
            print ("Customer details ......")
            print ("Customer code:",Ccode)
            print ("Customer name:",Cname)
            print ("Customer Id type:",Cid_type)
            print ("Customer Id Number:",Cid_no)
            print ("Customer address:",Cadd)
            print ("customer Nationality:",CNationality)
            print ("Check in date:",Cindate)
            print ("Check out date",Coutdate)
            print ("Room number:",Room_no)
            print ("Customer Contact number:",Ccontact_no)
        if (rec_count == 0):
            print("Record not found!!")
        db.commit()
        mycursor.close()
        db.close()
    else:
        print("Invalid Input!!")

def search():
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    Ccode = input("Enter Customer Code to be Searched in Hotel:")
    qry = "select * from hoteldata where Ccode=%s"
    rec_srch = (Ccode,)
    mycursor.execute(qry, rec_srch)
    rec_count = 0
    for(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,Room_rent,Food_bill,Laudry_bill,Game_bill,SubTotal_bill,Add_charges,GrandTotal_bill) in mycursor:
        rec_count += 1
        print ('Record  Found')
        print ("Customer details .....")
        print ("Customer code:",Ccode)
        print ("Customer name:",Cname)
        print ("Customer address:",Cadd)
        print ("Check in date:",Cindate)
        print ("Check out date",Coutdate)
        print ("Room number:",Room_no)
        print ("Room rent is:",Room_rent)
        print ("Food bill is:",Food_bill)
        print ("Laundary bill is:",Laudry_bill)
        print ("Game bill is:",Game_bill)
        print ("Sub total bill is:",SubTotal_bill)
        print ("Additional Service Charges is:",Add_charges)
        print ("Grand Total bill is:",GrandTotal_bill)
    if (rec_count == 0):
        print("Record not found!!")
    db.commit()
    mycursor.close()
    db.close()

def delete():
    global found
    found = 0
    db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    Ccode = int(input("Enter Customer Code to be delete from Hotel:"))
    qry = "delete from hoteldata where Ccode=%s"
    qry1 = "delete from customer where Ccode=%s"
    del_rec = (Ccode,)
    mycursor.execute('select * from hoteldata')
    tabsalt = mycursor.fetchall()
    for i in tabsalt:
        if i[0] == Ccode:
            found = 1
    if found == 1:
        mycursor.execute(qry, del_rec)
        mycursor.execute(qry1, del_rec)
        print('Record Deleted Successfully!!')
    else:
        print('Record not found!')
    db.commit()
    mycursor.close()
    db.close()

def update():
    print("Which Data Should be Updated .....")
    print("1.Customer Name:")
    print("2.Customer Address")
    print("3.Customer in Date")
    print("4.Customer Room Number")
    print("5.Customer Contact number")
    c = int(input("Select your Choice:"))
    if (c == 1):
        db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = input('Enter Code of Customer to be Updated:')
        qry = 'select * from hoteldata where Ccode=%s'
        Cname = input("Enter Customer Name:")
        q = 'update hoteldata set Cname=%s where Ccode=%s'
        data = (Cname, Ccode)
        mycursor.execute(q, data)
        q = 'update customer set Cname=%s where Ccode=%s'
        data = (Cname, Ccode)
        mycursor.execute(q, data)
        print('Record Updated .... ')
        db.commit()
        mycursor.close()
        db.close()
    elif (c == 2):
        db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('Enter Code of Customer to be Updated:'))
        qry = 'select * from hoteldata where Ccode=%s'
        Cadd = input("Enter Customer Address:")
        q = 'update hoteldata set Cadd=%s where Ccode=%s'
        data = (Cadd, Ccode)
        mycursor.execute(q, data)
        q = 'update customer set Cadd=%s where Ccode=%s'
        data = (Cadd, Ccode)
        mycursor.execute(q, data)
        print('Record Updated .... ')
        db.commit()
        mycursor.close()
        db.close()
    elif (c == 3):
        db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('Enter Code of Customer to be Updated:'))
        qry = 'select * from hoteldata where Ccode=%s'
        Cindate = str(input("Enter Customer in Date:"))
        q = 'update hoteldata set Cindate=%s where Ccode=%s'
        data = (Cindate, Ccode)
        mycursor.execute(q, data)
        q = 'update customer set Cindate=%s where Ccode=%s'
        data = (Cindate, Ccode)
        mycursor.execute(q, data)
        print('Record Updated .... ')
        db.commit()
        mycursor.close()
        db.close()
    elif (c == 4):
        db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('Enter Code of Customer to be Updated:'))
        qry = 'select * from hoteldata where Ccode=%s'
        Coutdate = input("Enter Customer out Date:")
        q = 'update hoteldata set Coutdate=%s where Ccode=%s'
        data = (Coutdate, Ccode)
        mycursor.execute(q, data)
        q = 'update customer set Coutdate=%s where Ccode=%s'
        data = (Coutdate, Ccode)
        mycursor.execute(q, data)
        print('Record Updated .... ')
        db.commit()
        mycursor.close()
        db.close()
    elif (c == 5):
        db = mysql.connector.connect(host='localhost', user='root', password='krmg1234', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = int(input('Enter Code of Customer to be Updated:'))
        qry = 'select * from customer where Ccode=%s'
        Ccontact_no = input("Enter Customer Contact number:")
        q = 'update customer set Ccontact_no=%s where Ccode=%s'
        data = (Ccontact_no, Ccode)
        mycursor.execute(q, data)
        print('Record Updated .... ')
        db.commit()
        mycursor.close()
        db.close()
    else:
        print("Invalid Input!!")

print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎░░WELCOME TO THE TAJ PALACE░░֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("Hello Customer!")
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
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.Speciality of your Hotel")
    print("2.Customer Management")
    print("3.EXIT")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    b = input("Enter your choice:")
    if (b == '1'):
        speciality()
    elif (b == '2'):
        hotelfarecal()
    elif (b == '3'):
        quit()
    else:
        print("Wrong Choice")
# End of the program