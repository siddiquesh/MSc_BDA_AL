-- ================================================================================
-- PRACTICAL 1: DATA SYSTEM FOR ANALYTICS (DSA)
-- TOPIC: WORKING WITH DDL AND DML COMMANDS (MySQL)
-- ================================================================================
-- FULL QUESTIONS:
-- Q. Working with DDL and DML Commands:
--    A - DDL (Data Definition Language) Commands:
--        1) Create Database and Table with Primary Key constraint.
--        2) Alter table structure (modify column constraints).
--        3) Drop Database and Table syntax.
--    B - DML (Data Manipulation Language) Commands:
--        1) Insert records into table (single and multi-row).
--        2) Select specific columns and all records from table.
--        3) Update specific records based on condition.
--        4) Delete specific records based on condition.
--    C - Operators:
--        1) Relational Operators (>, >=).
--        2) Arithmetic Operators (* 0.05 bonus calculation, alias).
--        3) Logical and Range Operators (&&, BETWEEN ... AND, IN).
--        4) LIKE Operator (Pattern matching with '%' and '_').
--        5) IS NULL and IS NOT NULL Operators, and updating NULL values.
-- ================================================================================

-- --------------------------------------------------------------------------------
-- PART A: DDL (DATA DEFINITION LANGUAGE) COMMANDS
-- --------------------------------------------------------------------------------

-- 1. CREATE DATABASE
CREATE DATABASE IF NOT EXISTS abdulwahab;
SHOW DATABASES;
USE abdulwahab;

-- 2. CREATE TABLE
CREATE TABLE IF NOT EXISTS employee (
    empid INT PRIMARY KEY,
    name CHAR(50),
    doj DATE,
    desgn CHAR(50),
    deptid VARCHAR(20)
);

-- Describe table schema
DESC employee;

-- 3. ALTER TABLE
-- Modify 'name' column to NOT NULL
ALTER TABLE employee MODIFY name CHAR(50) NOT NULL;
DESC employee;

-- 4. DROP SYNTAX (Reference)
-- DROP DATABASE <<db_name>>;
-- DROP TABLE <<table_name>>;


-- --------------------------------------------------------------------------------
-- PART B: DML (DATA MANIPULATION LANGUAGE) COMMANDS
-- --------------------------------------------------------------------------------

-- 1. INSERT COMMANDS
-- Single row insert with all columns
INSERT INTO employee VALUES (1, 'Alice', '2019-07-01', 'AS', 'D101');

-- Single row insert with specified columns
INSERT INTO employee (empid, name, doj, desgn, deptid) 
VALUES (2, 'Bob', '2020-01-04', 'AS', 'D104');

-- Multi-row insert
INSERT INTO employee VALUES
    (3, 'John', '2020-01-25', 'Professor', 'D101'),
    (4, 'Mary', '2015-03-05', 'HOD', 'D102'),
    (5, 'Sam', '2017-02-04', 'Professor', 'D102'),
    (6, 'Eric', '2019-08-17', 'Professor', 'D103'),
    (7, 'Andrew', '2018-09-20', 'HOD', 'D104');

-- 2. SELECT COMMANDS
-- Select specific columns
SELECT name, desgn FROM employee;

-- Select all columns
SELECT * FROM employee;

-- 3. UPDATE COMMAND
-- Update date of joining and designation for empid 1
UPDATE employee 
SET doj = '2019-09-08', desgn = 'AS' 
WHERE empid = 1;

SELECT * FROM employee;

-- 4. DELETE COMMAND
-- Delete record of employee where empid is 1
DELETE FROM employee WHERE empid = 1;

SELECT * FROM employee;


-- --------------------------------------------------------------------------------
-- PART C: OPERATORS
-- --------------------------------------------------------------------------------

-- Add salary column to demonstrate arithmetic and range queries
ALTER TABLE employee ADD COLUMN salary DECIMAL(10, 2);

-- Update salary values
UPDATE employee SET salary = 650000 WHERE empid = 2;
UPDATE employee SET salary = 800000 WHERE empid = 3;
UPDATE employee SET salary = 700000 WHERE empid = 4;
UPDATE employee SET salary = 500000 WHERE empid = 5;
UPDATE employee SET salary = 300000 WHERE empid = 6;
UPDATE employee SET salary = 700000 WHERE empid = 7;

-- 1. RELATIONAL OPERATORS
-- Select employees who joined after '2017-02-04'
SELECT * FROM employee WHERE doj > '2017-02-04';

-- Select employees where empid >= 4
SELECT name, empid FROM employee WHERE empid >= 4;

-- 2. ARITHMETIC OPERATORS
-- Calculate 5% of salary (e.g. bonus / tax deduction)
SELECT name, (salary * 0.05) AS bonus_component FROM employee;

-- Calculate total salary including 5% bonus with alias
SELECT name, (salary + salary * 0.05) AS Bonus FROM employee;

-- 3. LOGICAL AND RANGE OPERATORS
-- Filter by designation
SELECT * FROM employee WHERE desgn = 'HOD';

-- Relational AND operator (&& or AND)
SELECT * FROM employee WHERE salary >= 500000 && salary <= 800000;

-- BETWEEN ... AND operator
SELECT * FROM employee WHERE salary BETWEEN 500000 AND 800000;

-- IN operator
SELECT * FROM employee WHERE salary IN (300000, 500000, 800000);

-- --------------------------------------------------------------------------------
-- 4. LIKE OPERATOR (PATTERN MATCHING)
-- --------------------------------------------------------------------------------
-- Note: Standard table with 'ename' as column alias / name
-- Names starting with 'A'
SELECT * FROM employee WHERE name LIKE 'A%';

-- Names ending with 'b'
SELECT * FROM employee WHERE name LIKE '%b';

-- Names containing letter 'a' (case-insensitive in MySQL)
SELECT * FROM employee WHERE name LIKE '%a%';

-- Names where second character is 'o'
SELECT * FROM employee WHERE name LIKE '_o%';

-- Names where second last character is 'r'
SELECT * FROM employee WHERE name LIKE '%r_';

-- Names containing 'i' followed by exactly two characters
SELECT * FROM employee WHERE name LIKE '%i__';

-- Names having exactly 4 letters
SELECT * FROM employee WHERE name LIKE '____';

-- --------------------------------------------------------------------------------
-- 5. IS NULL AND IS NOT NULL OPERATORS
-- --------------------------------------------------------------------------------
-- Insert a record with NULL department to test NULL checks
INSERT INTO employee (empid, name, doj, desgn, deptid, salary) 
VALUES (8, 'Samir', '2021-01-25', 'AS', NULL, 700000.00);

-- Find employees with no assigned department (deptid IS NULL)
SELECT * FROM employee WHERE deptid IS NULL;

-- Find employees with an assigned department (deptid IS NOT NULL)
SELECT * FROM employee WHERE deptid IS NOT NULL;

-- Fill/Update NULL values with department 'D103'
UPDATE employee SET deptid = 'D103' WHERE deptid IS NULL;

-- Verify all employees have department assigned
SELECT * FROM employee;
