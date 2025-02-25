# -*- coding: utf-8 -*-
'''
Library Management System.

This module organizes all of the libraries physical and digital assets, in
addition to their relationships with their members.

Features:
- Member registration and management
- Book catalog and inventory management
- Author information management
- Database structure modification
- Data filtering and retrieval

Usage:
  Run this script directly to start the library management system
  Follow the on-screen prompts to navigate through different functions

'''
__author__ = "Pavan Kannan"
__copyright__ = "(c) Copyright Pavan Kannan 2022"
__maintainer__ = "GEMS New Millennium School"
__email__ = "pavan.2k23@gmail.com"
__version__ = "1.0.0"

# Standard library imports
from tabulate import tabulate  # For formatted table display

# Third party imports
import mysql.connector  # Database connector for MySQL

# Local application imports
# None

# =====================================================================
# DATABASE CONNECTION SETUP
# =====================================================================

print("Creating database connection")
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="gems"
)

print("Creating db cursor")
mycursor = db.cursor()

# =====================================================================
# UTILITY FUNCTIONS
# =====================================================================

def border():
    """Display a horizontal border line for better UI separation."""
    print("==========================================")
    
# =====================================================================
# DATA ENTRY FUNCTIONS
# =====================================================================

def members():
    """
    Register a new library member.
    
    Collects member information and inserts it into the members table.
    """
    border()
    adarid = input("Enter Emirates ID: ")
    mem_name = input("Enter Member name: ")
    mem_no = int(input("Enter Member Phone Number: "))
    print(" Task Performed Successfully")
    mycursor.execute(
        "INSERT INTO members(member_id, name, contact_no) VALUES(%s, %s, %s)",
        (adarid, mem_name, mem_no))
    db.commit()
    main()


def books():
    """
    Register a new book in the library catalog.
    
    Collects book information and inserts it into the books table.
    """
    border()
    bookname = input("Enter Book name: ")
    stock_avail = int(input("Enter number of books available: "))
    auth_id = int(input("Enter Author ID: "))
    bookgenre = input("Enter Book Genre: ")
    print(" Task Performed Successfully")
    mycursor.execute("INSERT INTO books (author_id, book_name, stock, genre) VALUES(%s, %s, %s, %s)",
                     (auth_id, bookname, stock_avail, bookgenre))
    db.commit()
    main()


def authors():
    '''
    Register a new author in the system.
    
    Collects author information and inserts it into the authors table.
    '''
    border()
    auth_name = input("Enter Author name: ")
    auth_cont_id = input("Enter Author Contact: ")
    auth_id = int(input("Enter Author ID: "))
    print(" Task Performed Successfully")
    mycursor.execute("INSERT INTO authors(author_int, author_name, author_contact) VALUES(%s, %s,%s)", 
                    (auth_id, auth_name, auth_cont_id))
    db.commit()
    main()

# =====================================================================
# FILTER SELECTION FUNCTIONS
# =====================================================================

def memberfilter():
    """
    Display members table columns and get user's column selection.
    
    Returns:
        str: The selected column name
    """
    result = []
    border()
    print(tabulate(result, headers=['member_id', 'name', 'contact_no'], tablefmt='psql'))
    column_filter = input("Select a Column: ")
    print(column_filter)
    return column_filter


def bookfilter():
    """
    Display books table columns and get user's column selection.
    
    Returns:
        str: The selected column name
    """
    result = []
    border()
    print(tabulate(result, headers=['author_id', 'book_name', 'stock', 'genre'], tablefmt='psql'))
    column_filter = input("Select a Column: ")
    print(column_filter)
    return column_filter


def authorfilter():
    """
    Display authors table columns and get user's column selection.
    
    Returns:
        str: The selected column name
    """
    result = []
    border()
    print(tabulate(result, headers=['author_id', 'author_name', 'author_contact'], tablefmt='psql'))
    column_filter = input("Select a Column: ")
    print(column_filter)
    return column_filter

# =====================================================================
# DATA FILTERING SYSTEM
# =====================================================================

def filtersys():
    """
    Filter and display data from the selected table and column.
    
    Allows users to select specific data columns to view.
    """
    border()
    print("members\t(m)\nbooks\t(b)\nauthors\t(a)")
    database = input("Choice an Table: ")

    if database == "m":
        filter_val = memberfilter()
        print("Selected column is", filter_val)
        mycursor.execute("SELECT {0} FROM members".format(filter_val))
        if filter_val == 'member_id':
            filter_val = 'MEMBER ID'
        elif filter_val == 'name':
            filter_val = 'NAME'
        elif filter_val == 'contact_no':
            filter_val = 'CONTACT NUMBER'
        result = mycursor.fetchall()
        print(tabulate(result, headers=[filter_val], tablefmt='psql'))
        main()

    elif database == "b":
        filter_val = bookfilter()
        border()
        print("Selected column is", filter_val)
        mycursor.execute("SELECT {0} FROM books".format(filter_val))
        if filter_val == 'author_id':
            filter_val = 'AUTHOR ID'
        elif filter_val == 'book_name':
            filter_val = 'BOOK_NAME'
        elif filter_val == 'stock':
            filter_val = 'STOCK'
        elif filter_val == 'genre':
            filter_val = 'GENRE'
        result = mycursor.fetchall()
        print(tabulate(result, headers=[filter_val], tablefmt='psql'))
        main()

    elif (database == "a"):
        filter_val = authorfilter()
        border()
        print("Selected column is", filter_val)
        mycursor.execute("SELECT {0} FROM authors".format(filter_val))
        if filter_val == 'author_id':
            filter_val = 'AUTHOR ID'
        elif filter_val == 'author_name':
            filter_val = 'AUTHOR_NAME'
        elif filter_val == 'author_contact':
            filter_val = 'AUTHOR CONTACT NUMBER'
        result = mycursor.fetchall()
        print(tabulate(result, headers=[filter_val], tablefmt='psql'))
        main()

    else:
        main()
    main()

# =====================================================================
# DATABASE STRUCTURE MODIFICATION SYSTEM
# =====================================================================

def altersys():
    """
    Modify the database structure.
    
    Allows users to add, modify, or delete columns from tables.
    """
    border()
    print("members\t(m)\nbooks\t(b)\nauthors\t(a)")
    table_name = input("Choice a Table: ")
    if table_name == 'm':
        table_name = 'members'
    elif table_name == 'b':
        table_name = 'books'
    elif table_name == 'a':
        table_name = 'authors'   
    border()
    print("Modify\t(m)\nDrop\t(d)")
    mdfy = input("Enter your option: ")

    if (mdfy == "m"):
        border()
        print("Add new column (a) or Change (c)")
        addchg = input("Enter your option: ")

        if addchg == "a":
            mycursor.execute("DESC {0}".format(table_name))
            result = mycursor.fetchall()
            border()
            print(tabulate(result, tablefmt='psql'))
            column_name = input("Enter new column name: ")
            col_datatype = input("Enter column datatype: ")
            mycursor.execute("ALTER TABLE {0} ADD COLUMN {1} {2}".format(
                table_name, column_name, col_datatype))
            mycursor.execute("DESC {0}".format(table_name))
            result = mycursor.fetchall()
            print(tabulate(result, tablefmt='psql'))
            db.commit()

        elif addchg == "c":
            mycursor.execute("DESC {0}".format(table_name))
            result = mycursor.fetchall()
            border()
            print(tabulate(result, tablefmt='psql'))
            oldcolumn_name = input("Enter old column name: ")
            newcolumn_name = input("Enter new column name: ")
            col_datatype = input("Enter column datatype: ")
            mycursor.execute("ALTER TABLE {0} CHANGE {1} {2} {3}".format(
                table_name, oldcolumn_name, newcolumn_name, col_datatype))
            mycursor.execute("DESC {0}".format(table_name))
            result = mycursor.fetchall()
            print(tabulate(result, tablefmt='psql'))
            db.commit()

        else:
            main()

    elif mdfy == "d":
        mycursor.execute("DESC {0}".format(table_name))
        result = mycursor.fetchall()
        border()
        print(tabulate(result, tablefmt='psql'))
        column_name = input("Enter deleting column name: ")
        mycursor.execute("ALTER TABLE {0} DROP {1}".format(
            table_name, column_name))
        mycursor.execute("DESC {0}".format(table_name))
        result = mycursor.fetchall()
        print(tabulate(result, tablefmt='psql'))
        db.commit()

    else:
        main()
    main()

# =====================================================================
# DATA VIEWING FUNCTION
# =====================================================================

def viewtab():
    """
    View all records from a selected table.
    
    Displays all records in a formatted table.
    """
    border()
    print("members\t(m)\nbooks\t(b)\nauthors\t(a)")
    table_name = input("Choice a Table: ")
    if table_name == "m":
        mycursor.execute("SELECT * FROM members")
        result = mycursor.fetchall()
        print(tabulate(result, headers=['MEMBER ID', 'NAME', 'CONTACT NUMBER'], tablefmt='psql'))
        

    elif table_name == "b":
        mycursor.execute("SELECT * FROM books")
        result = mycursor.fetchall()
        print(tabulate(result, headers=['AUTHOR ID', 'BOOK NAME', 'STOCK', 'GENRE'], tablefmt='psql'))
        
    elif table_name == "a":
        mycursor.execute("SELECT * FROM authors")
        result = mycursor.fetchall()
        print(tabulate(result, headers=['AUTHOR ID', 'AUTHOR NAME', 'AUTHOR CONTACT NUMBER'], tablefmt='psql'))
    else:
        main()
    main()

# =====================================================================
# MAIN FUNCTION - APPLICATION ENTRY POINT
# =====================================================================

def main():
    """
    Main function that controls the application flow.
    
    Displays the main menu and directs to specific functions based on user input.
    """
    border()
    print("Welcome to the Library Management Database")
    print("------------------------------------------")
    usr_func = input(
        "ADD DATA\t\t(a)\nMODIFY DATA\t\t(m)\nFILTER DATA\t\t(f)\nVIEW DATA\t\t(v)\nQUIT\t\t\t(q)\n>>>")
    db.commit()
    if usr_func == "a":
        border()
        print("Register Member\t\t(m)\nRegister Book\t\t(b)\nResgister Author\t(i)")
        exe_func = input("Enter your option: ")

        if exe_func == "m":
            members()

        elif exe_func == "b":
            books()

        elif exe_func == "i":
            authors()

        else:
            main()

    elif usr_func == "m":
        altersys()

    elif usr_func == "f":
        filtersys()

    elif usr_func == "v":
        viewtab()

    elif usr_func == "q":
        print("DEVELOPED BY: PAVAN & MOHIT")
        quit()

    else:
        main()


# Start the application if this script is run directly
if __name__ == "__main__":
    main()
