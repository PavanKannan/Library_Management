#import
import mysql.connector
from datetime import datetime

#connecting mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Library_DB"
)

mycursor = db.cursor()

# CREATING TABLES AND FUNCTIONS

#mycursor.execute("CREATE DATABASE Library_DB")
#mycursor.execute("CREATE TABLE MEMBERDATA (membershipID int PRIMARY KEY AUTO_INCREMENT, name varchar(50), contact_no int, registered datetime)")
#mycursor.execute("CREATE TABLE BOOKDATA (BOOKID int PRIMARY KEY AUTO_INCREMENT, Book_name varchar(50), AuthorID int,STOCK int, Genre Varchar(50))")
#mycursor.execute("CREATE TABLE AUTHORINFO (AuthorID int PRIMARY KEY AUTO_INCREMENT, Author_Name varchar(50), Author_contact varchar(50)) ")


# Enter new values 
def memberdata():
    cname = input("Enter Member name: ")
    phone_no = int(input("Enter Member Phone Number: "))
    mycursor.execute("INSERT INTO MEMBERDATA (name, contact_no, registered) VALUES (%s, %s, %s)", (cname, phone_no, datetime.now()))
    db.commit()

def bookdata():
    bookname = input("Enter Book name: ")
    Stock_avail = int(input("Enter number of books available: "))
    Auth_id = int(input("Enter Author ID: "))
    bookgenre = input("Enter Book Genre: ")
    mycursor.execute("INSERT INTO BOOKDATA (book_name, AuthorID, STOCK, Genre) VALUES (%s, %s, %s, %s)", (bookname, Auth_id, Stock_avail, bookgenre))
    db.commit()

def authorinfo():
    aname = input("Enter Author name: ")
    contact_id = input("Enter Author Contact: ")
    mycursor.execute("INSERT INTO AUTHORINFO (Author_Name, Author_contact) VALUES (%s, %s)", (aname, contact_id))
    db.commit()

# Select system
def memberfilter():
    mycursor.execute("DESCRIBE MEMBERDATA")
    column_filter = input("Choice a Column: ")
    return

def bookfilter():
    mycursor.execute("DESCRIBE BOOKDATA")
    column_filter = input("Choice a Column: ")
    return

def authorfilter():
    mycursor.execute("DESCRIBE AUTHORINFO")
    column_filter = input("Choice a Column: ")
    return

# Filter system
def filter():
    
    print ("MEMBERDATA\t(m)\nBOOKDATA\t(b)\nAUTHORINFO\t(a)")
    database = input("Choice an Table: ")
    
    if (database == "m"):
        filter_val = memberfilter()
        mycursor.execute("SELECT %s FROM MEMBERDATA", (filter_val))
        result = mycursor.fetchall()
        for x in result:
            print(x)
    
    elif (database == "b"):
        filter_val = bookfilter()
        mycursor.execute("SELECT %s FROM BOOKDATA", (filter_val))
        result = mycursor.fetchall()
        for x in result:
            print(x)
    
    elif (database == "a"):
        filter_val = authorfilter()
        mycursor.execute("SELECT %s FROM AUTHORDATA", (filter_val))
        result = mycursor.fetchall()
        for x in result:
            print(x)
    
    else:
        usrint()



# Alteration System
def altersys():

    print ("MEMBERDATA\t(m)\nBOOKDATA\t(b)\nAUTHORINFO\t(a)")
    table_name = input("Choice a Table: ")
    print("Modify\t(m)\nDrop\t(d)")
    modro = input("Enter your option: ")

    if (modro == "m"):
        print("Add new column (a) or Change (c)")
        addchg = input("Enter your option: ")
    
        if (addchg == "a"):
            mycursor.execute("DESCRIBE %s", (table_name))
            column_name = input ("Enter new column name: ")
            col_datatype = input("Enter column datatype: ")
            mycursor.execute("ALTER TABLE {0} ADD COLUMN {1} {2}".format(table_name, column_name, col_datatype))
            mycursor.execute("DESCRIBE %s", (table_name))
            db.commit()
    
        elif(addchg == "c"):
            mycursor.execute("DESCRIBE %s", (table_name))
            oldcolumn_name = input ("Enter old column name: ")
            newcolumn_name = input ("Enter new column name: ")
            col_datatype = input("Enter column datatype: ")
            mycursor.execute("ALTER TABLE {0} CHANGE {1} {2} {3}".format(table_name, oldcolumn_name, newcolumn_name, col_datatype))
            mycursor.execute("DESCRIBE %s", (table_name))
            db.commit()

        else:
            usrint()    
        
    elif (modro == "d"):
        mycursor.execute("DESCRIBE %s", (table_name))
        column_name = input ("Enter deleting column name: ")
        mycursor.execute("ALTER TABLE {0} DROP {1}".format(table_name, column_name))
        db.commit()

    else:
        usrint()

#View tables
def viewtab():
    print ("MEMBERDATA\t(m)\nBOOKDATA\t(b)\nAUTHORINFO\t(a)")
    table_name = input("Choice a Table: ")
    if (table_name == "m"):
        mycursor.execute("SELECT * FROM MEMBERDATA")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    elif (table_name == "b"):
        mycursor.execute("SELECT * FROM BOOKDATA")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    elif (table_name == "a"):
        mycursor.execute("SELECT * FROM AUTHORINFO")
        result = mycursor.fetchall()
        for x in result:
            print(x)
            
    else:
        usrint()
    

def usrint():
    
    print("Welcome to the Library Management Database")
    usr_func = input ("Add data\t\t(a)\nmodify data\t\t(m)\nsearch or filter\t(f)\nview data\t\t(v)\nquit\t\t\t(q)\n")
    db.commit
    if (usr_func == "a"):
        print("New Member?\t(m)\nNew Book?\t(b)\nAuthor info\t(i)")
        exe_func = input("Enter your option: ")
        
    
        if (exe_func == "m"):
            memberdata()
    
        elif(exe_func == "b"):
            bookdata()
    
        elif (exe_func == "i"):
            authorinfo()
    
        else:
            usrint()
    
    elif(usr_func == "m"):
        altersys()
    
    elif (usr_func == "f"):
        filter()
    
    elif (usr_func == "v"):
        viewtab()
    
    elif (usr_func == "q"):
        quit()
    
    else:
        usrint()

        
usrint()   