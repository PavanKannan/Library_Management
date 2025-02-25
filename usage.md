# GEMS Library Management System - Usage Guide

## Introduction

The GEMS Library Management System is a command-line application designed to help manage a library's resources including members, books, and authors. This guide will help you understand how to use the system effectively.

## Getting Started

1. Make sure you have Python and MySQL installed
2. Create the database using the SQL script: `mysql -u root -p < gems_lms.sql`
3. Install required dependencies: `pip install -r requirements.txt`
4. Run the application: `python library_management_system.py`

## Main Menu

When you start the application, you'll see the main menu with these options:

```
ADD DATA        (a)
MODIFY DATA     (m)
FILTER DATA     (f)
VIEW DATA       (v)
QUIT            (q)
```

## Adding Data

To add new records, select option (a) from the main menu, then choose:

- **Register Member (m)**: Add a new library member
- **Register Book (b)**: Add a new book to the inventory
- **Register Author (i)**: Add a new author

### Adding a Member

You'll need to provide:
- Emirates ID
- Member name
- Phone number

### Adding a Book

You'll need to provide:
- Book name
- Number of books available (stock)
- Author ID (must exist in the authors table)
- Book genre

### Adding an Author

You'll need to provide:
- Author ID
- Author name
- Author contact information

## Viewing Data

To view all records in a table, select option (v) from the main menu, then choose:

- **members (m)**: View all library members
- **books (b)**: View all books
- **authors (a)**: View all authors

## Filtering Data

To filter and view specific columns, select option (f) from the main menu, then:

1. Choose the table to filter
2. Select the column you want to view
3. The system will display only that column's data

## Modifying Database Structure

To modify the database structure, select option (m) from the main menu, then:

1. Choose the table to modify
2. Select Modify (m) or Drop (d)
3. If modifying, choose to Add (a) or Change (c) a column
4. Follow the prompts to make your changes

## Exiting the System

Select option (q) from the main menu to quit the application.

## Support

For any issues or questions, please contact:
- Pavan Kannan (pavan.2k23@gmail.com)
