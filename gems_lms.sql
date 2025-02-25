/* 
   DDL statements for GEMS Library Management System
   
   This script creates the database structure for the library management system
   including tables for members, books, and authors.
*/

-- Create database gems
CREATE DATABASE IF NOT EXISTS gems;

-- Use the gems database
USE gems;

-- Create table members
-- Stores information about library members
CREATE TABLE IF NOT EXISTS gems.members (
 member_id smallint PRIMARY KEY,         -- Unique identifier for members (Emirates ID)
 name varchar(60) NOT NULL,              -- Member's full name
 contact_no varchar(15) NOT NULL         -- Member's contact number
);

-- Create table books
-- Stores information about books in the library
CREATE TABLE IF NOT EXISTS gems.books (
 author_id smallint,                    -- Foreign key referencing authors
 book_name varchar(100) NOT NULL,       -- Name/title of the book
 stock smallint NOT NULL,               -- Number of copies available
 genre varchar(50)                      -- Book genre category
);

-- Create table authors
-- Stores information about book authors
CREATE TABLE IF NOT EXISTS gems.authors (
 author_id smallint PRIMARY KEY,         -- Unique identifier for authors
 autor_name varchar(100) NOT NULL,       -- Author's name (Note: typo in column name)
 author_contact varchar(100)             -- Author's contact information
);

-- Note: Additional indexes and constraints could be added for better performance
-- and data integrity in a production environment
