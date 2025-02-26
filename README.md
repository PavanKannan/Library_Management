# Library Management System  

## Overview  
The **Library Management System** is a Python-based application designed to manage a library’s physical and digital assets efficiently. It handles member registration, book inventory management, author information, and database modifications.  

## Features  
- **Member Management** – Register and manage library members.  
- **Book Inventory** – Add, update, and track book availability.  
- **Author Management** – Store and manage author details.  
- **Data Filtering** – Retrieve and display specific records using filters.  
- **Database Modifications** – Modify the structure of tables (add, update, or delete columns).  

## Technologies Used  
- **Python**  
- **MySQL** (Database)  
- **tabulate** (For formatted table display)  

## Setup Instructions  

### Prerequisites  
- Install Python 3.x  
- Install MySQL and create a database named `gems`  
- Install required Python libraries:  
  ```bash
  pip install mysql-connector-python tabulate
  ```

### Database Setup  
1. Import the **gems_lms.sql** file into MySQL:  
   ```bash
   mysql -u root -p < gems_lms.sql
   ```
2. Update the **database connection** in `library_management_system.py` if necessary:  
   ```python
   db = mysql.connector.connect(
       host="localhost",
       port=3306,
       user="root",
       passwd="root",
       database="gems"
   )
   ```

### Running the Application  
Run the Python script:  
```bash
python library_management_system.py
```

## Usage  
1. Select an option from the menu:  
   - **Add Data**: Register members, books, or authors.  
   - **Modify Data**: Alter database structure.  
   - **Filter Data**: Retrieve specific records.  
   - **View Data**: Display all records in a table format.  
   - **Quit**: Exit the program.  

## Contributors  
- **Pavan Kannan**  
- **Mohit**  

## License  
This project is licensed under [MIT License](LICENSE).  
