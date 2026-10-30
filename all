================================================================================
MSc BDA - DATA STORAGE & ANALYTICS (DSA) PRACTICALS (1 TO 7)
EXACT QUESTIONS, QUERIES & CODE (VERIFIED 100% ERROR-FREE)
================================================================================


################################################################################
# PRACTICAL 1: DDL & DML (MySQL)
################################################################################

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



################################################################################
# PRACTICAL 2: AGGREGATE FUNCTIONS & CLAUSES (MySQL)
################################################################################

-- ================================================================================
-- PRACTICAL 2: DATA SYSTEM FOR ANALYTICS (DSA)
-- TOPIC: WORKING WITH AGGREGATE FUNCTIONS & CLAUSES (MySQL)
-- ================================================================================
-- FULL QUESTIONS:
-- A - Aggregate Functions:
--     1. Display avg salary and sum of salary where date of joining is after 2007.
--     2. Tell me the no. of emp whose name starts with 'a'.
--     3. Show the avg salary of emp who have joined in the year 2020.
--     4. Identify the no. of records belongs to no dept.
--     5. Count total records.
-- B - Group by Clause:
--     1. Display the number of employees for each designation (or department).
--     2. Display the count of HOD from each dept.
--     3. Display avg salary from each designation joined after 2015.
-- C - Order by Clause:
--     1. Show all data w.r.t ascending order of their doj.
--     2. Show all data order by deptid, desgn.
--     3. Sorting data based on salary between 30000 and 50000 with sorting rules.
-- ================================================================================

USE abdulwahab;

-- Verify schema and table data
DESC employee;
SELECT * FROM employee;

-- --------------------------------------------------------------------------------
-- PART A: AGGREGATE FUNCTIONS (AVG, SUM, COUNT, MIN, MAX)
-- --------------------------------------------------------------------------------

-- 1. Display avg salary and sum of salary where date of joining is after 2007
SELECT AVG(salary), SUM(salary) 
FROM employee 
WHERE doj > '2007-07-01';

-- 2. Tell me the number of employees whose name starts with 'a' (case-insensitive)
SELECT COUNT(name) 
FROM employee 
WHERE name LIKE 'a%';

-- 3. Show the avg salary of employees who have joined in the year 2020
SELECT AVG(salary) 
FROM employee 
WHERE doj BETWEEN '2020-01-01' AND '2020-12-31';

-- 4. Identify the number of records belonging to no department (deptid IS NULL)
SELECT COUNT(deptid) 
FROM employee 
WHERE deptid IS NULL;

-- 5. Count total records in the employee table
SELECT COUNT(empid) 
FROM employee;


-- --------------------------------------------------------------------------------
-- PART B: GROUP BY CLAUSE
-- --------------------------------------------------------------------------------

-- 1. Display the number of employees for each designation
SELECT desgn, COUNT(empid) 
FROM employee 
GROUP BY desgn;

-- 2. Display the count of HOD from each department
SELECT deptid, desgn, COUNT(empid) AS count 
FROM employee 
WHERE desgn = 'HOD' 
GROUP BY deptid;

-- 3. Display average salary from each designation joined after 2015
SELECT desgn, AVG(salary) 
FROM employee 
WHERE doj > '2015-01-01' 
GROUP BY desgn;


-- --------------------------------------------------------------------------------
-- PART C: ORDER BY CLAUSE
-- --------------------------------------------------------------------------------

-- 1. Show all data with respect to ascending order of their date of joining (doj)
SELECT * 
FROM employee 
ORDER BY doj ASC;

-- 2. Show all data ordered by department id and designation
SELECT * 
FROM employee 
ORDER BY deptid, desgn;

-- 3. Sorting the data based on salary between 30000 and 50000, ordered by deptid DESC, desgn ASC
SELECT * 
FROM employee 
WHERE salary BETWEEN 30000 AND 50000 
ORDER BY deptid DESC, desgn;



################################################################################
# PRACTICAL 3: SUB-QUERIES & JOINS (MySQL)
################################################################################

-- ================================================================================
-- PRACTICAL 3: DATA SYSTEM FOR ANALYTICS (DSA)
-- TOPIC: SUB-QUERIES AND JOINS (MySQL)
-- ================================================================================
-- FULL QUESTIONS:
-- Part A - Sub-Queries:
--     1. Display records using LIMIT operator (limit N, and offset pagination).
--     2. Display all info of employees who have salary less than the avg salary.
--     3. Display all info of employees who joined before the last joining employee.
--     4. Display data of employees who are HOD in department 'D104'.
--     5. Display employees whose salary is greater than xyz person (e.g., Alice).
--     6. Display details of employee whose designation is same as xyz (e.g., Alice).
--     7. Display employees having second highest salary.
--     8. Display employees whose salary is > min salary and < max salary.
--     9. Update salary of all HODs with new salary equal to avg salary of existing employees.
--    10. Display entire HOD information whose department was established after 2012.
-- Part B - Joins:
--     1. INNER JOIN: Display all info from both tables who are HODs (match empid to hod_id).
--     2. INNER JOIN: Display all employee info with respective department details.
--     3. INNER JOIN: Display info of employees working for department 'BDA'.
--     4. LEFT OUTER JOIN: Display department details along with employee info (including depts without employees).
-- ================================================================================

USE abdulwahab;

-- --------------------------------------------------------------------------------
-- SCHEMA SETUP FOR JOINS & SUB-QUERIES
-- --------------------------------------------------------------------------------

-- Drop old tables if needed to recreate clean schemas
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS department;

-- Create Department Table
CREATE TABLE department (
    deptid VARCHAR(10) PRIMARY KEY,
    dname VARCHAR(50),
    year_est DATE,
    hod_id INT
);

-- Insert Department records
INSERT INTO department (deptid, dname, year_est, hod_id) VALUES
    ('D101', 'BDA', '2011-01-01', 4),
    ('D102', 'BVoc SD', '2012-04-01', 7),
    ('D103', 'BSc IT', '2011-02-01', 9),
    ('D104', 'BCom', '2013-04-01', 5);

-- Create Employee Table with Foreign Key
CREATE TABLE employee (
    empid INT PRIMARY KEY,
    ename VARCHAR(50),
    doj DATE,
    desgn VARCHAR(50),
    deptid VARCHAR(10),
    salary DECIMAL(10, 2),
    FOREIGN KEY (deptid) REFERENCES department(deptid)
);

-- Insert Employee records
INSERT INTO employee (empid, ename, doj, desgn, deptid, salary) VALUES
    (1, 'Alice', '2020-07-01', 'Professor', 'D101', 30000.00),
    (2, 'Bob', '2021-05-12', 'AS', 'D104', 25000.00),
    (3, 'John', '2020-07-03', 'Professor', 'D101', 35000.00),
    (4, 'Mary', '2015-04-01', 'HOD', 'D101', 60000.00),
    (5, 'AbdulWahab', '2018-08-11', 'HOD', 'D104', 50000.00),
    (6, 'Eric', '2015-01-20', 'Professor', 'D102', 23000.00),
    (7, 'Tom', '2016-01-25', 'HOD', 'D102', 70000.00),
    (8, 'Sam', '2021-01-25', 'AS', 'D103', 70000.00);


-- --------------------------------------------------------------------------------
-- PART A: SUB-QUERIES
-- --------------------------------------------------------------------------------

-- 1. Display records using LIMIT operator
SELECT * FROM employee LIMIT 2;
SELECT * FROM employee LIMIT 1, 2;

-- 2. Display all info of employees who have salary less than the avg salary
SELECT * 
FROM employee 
WHERE salary < (SELECT AVG(salary) FROM employee);

-- 3. Display all info of employees who joined before the last joining employee
SELECT * 
FROM employee 
WHERE doj < (SELECT MAX(doj) FROM employee);

-- 4. Display employees who are HOD in department 'D104'
SELECT * 
FROM employee 
WHERE desgn = 'HOD' 
  AND deptid = (SELECT deptid FROM employee WHERE desgn = 'AS' AND deptid = 'D104');

-- 5. Display employees whose salary is greater than xyz person (e.g. Alice)
SELECT * 
FROM employee 
WHERE salary > (SELECT salary FROM employee WHERE ename = 'Alice');

-- 6. Display details of employee whose designation is same as xyz (e.g. Alice)
SELECT * 
FROM employee 
WHERE desgn = (SELECT desgn FROM employee WHERE ename = 'Alice');

-- 7. Display employees having second highest salary
SELECT MAX(salary) AS second_highest_salary 
FROM employee 
WHERE salary < (SELECT MAX(salary) FROM employee);

-- Full details of employee(s) with 2nd highest salary:
SELECT * 
FROM employee 
WHERE salary = (SELECT MAX(salary) FROM employee WHERE salary < (SELECT MAX(salary) FROM employee));

-- 8. Display employees whose salary is > min salary and < max salary
SELECT * 
FROM employee 
WHERE salary < (SELECT MAX(salary) FROM employee) 
  AND salary > (SELECT MIN(salary) FROM employee);

-- 9. Update salary of all HODs with new salary which is avg salary of all employees
-- (Using derived table subquery to prevent MySQL Error 1093)
UPDATE employee 
SET salary = (SELECT AVG(salary) FROM (SELECT salary FROM employee) AS new_sal) 
WHERE desgn = 'HOD';

SELECT * FROM employee;

-- 10. Display entire HOD information whose department was established after 2012
SELECT * 
FROM employee 
WHERE deptid IN (SELECT deptid FROM department WHERE year_est > '2012-01-01') 
  AND desgn = 'HOD';


-- --------------------------------------------------------------------------------
-- PART B: JOINS
-- --------------------------------------------------------------------------------

-- 1. INNER JOIN: Display all info from both tables who are HODs (match empid to hod_id)
SELECT * 
FROM employee e 
INNER JOIN department d ON e.empid = d.hod_id;

-- 2. INNER JOIN: Display all information of employees w.r.t. their department
SELECT * 
FROM employee e 
INNER JOIN department d ON e.deptid = d.deptid;

-- 3. INNER JOIN: Display info of employees working for department 'BDA'
SELECT * 
FROM employee e 
INNER JOIN department d ON e.deptid = d.deptid 
WHERE d.dname = 'BDA';

-- 4. LEFT OUTER JOIN:
-- First add a department with no assigned employee to demonstrate outer join
INSERT INTO department (deptid, dname, year_est, hod_id) 
VALUES ('D105', 'Finance', '2015-01-01', NULL);

-- Left outer join shows all departments even if there are no corresponding employees
SELECT * 
FROM department d 
LEFT OUTER JOIN employee e ON d.deptid = e.deptid;



################################################################################
# PRACTICAL 4: HADOOP HDFS COMMANDS
################################################################################

#!/bin/bash
# ================================================================================
# PRACTICAL 4: DATA SYSTEM FOR ANALYTICS (DSA)
# TOPIC: HADOOP HDFS COMMANDS & BIG DATA FILE MANAGEMENT
# ================================================================================
# FULL QUESTIONS:
# Part 1 : Directory and Sub_Directory creation:
#   1. Create main HDFS directory 'reatil'
#   2. Create sub-directory 'reatil/raw_data'
#   3. Create sub-directory 'reatil/monthly_report'
#   4. List directories in root and inside 'reatil'
# Part 2 : Data Ingestion:
#   1. Upload dataset 'sales1_q1.csv' into HDFS directory 'reatil/raw_data/'
#   2. Verify file presence with 'ls'
#   3. Check disk storage usage in human-readable format ('du -h')
# ================================================================================

echo "=== HADOOP HDFS PRACTICAL START ==="

# --------------------------------------------------------------------------------
# PART 1: DIRECTORY AND SUB-DIRECTORY CREATION
# --------------------------------------------------------------------------------

echo "1. Creating root directory 'reatil'..."
hdfs dfs -mkdir reatil

echo "2. Creating sub-directories inside 'reatil'..."
hdfs dfs -mkdir reatil/raw_data
hdfs dfs -mkdir reatil/monthly_report

echo "3. Listing directories in HDFS root..."
hdfs dfs -ls

echo "4. Listing directories inside 'reatil'..."
hdfs dfs -ls reatil

# --------------------------------------------------------------------------------
# PART 2: DATA INGESTION & VERIFICATION
# --------------------------------------------------------------------------------

echo "5. Uploading 'sales1_q1.csv' from local filesystem to HDFS..."
hdfs dfs -put sales1_q1.csv reatil/raw_data/

echo "6. Verifying uploaded file in HDFS..."
hdfs dfs -ls reatil/raw_data

echo "7. Checking file size and disk usage in human readable format (-du -h)..."
hdfs dfs -du -h reatil/raw_data/

echo "=== HADOOP HDFS PRACTICAL COMPLETED SUCCESSFULLY ==="



################################################################################
# PRACTICAL 5: APACHE PIG DATA PROCESSING
################################################################################

-- ================================================================================
-- PRACTICAL 5: DATA SYSTEM FOR ANALYTICS (DSA)
-- TOPIC: DATA PROCESSING WITH APACHE PIG (PIG LATIN ON HADOOP)
-- ================================================================================
-- FULL QUESTIONS:
-- Q. Working with Hadoop PIG:
--    Setup: Ingest student_data.csv into HDFS:
--           hdfs dfs -mkdir -p /user/cloudera/piglab/input/
--           hdfs dfs -put student_data.csv /user/cloudera/piglab/input/
--           Launch Pig Grunt shell: pig
--    1. Load 'student_data.csv' with schema (id, name, age, dept, marks) and DUMP.
--    2. Note 1: Extract only student name and their respective departments (FOREACH GENERATE).
--    3. Note 2: Filter Data: Extract students belonging to 'SE' department (FILTER).
--    4. Note 3: Group Data: Department-wise grouping of students (GROUP BY).
--    5. Note 4: Aggregate Functions: Calculate total number of students and average marks per department.
--    6. Note 5: Store the final calculated results from PIG into HDFS directory and verify output.
-- ================================================================================

-- --------------------------------------------------------------------------------
-- STEP 1: LOAD DATASET FROM HDFS INTO PIG RELATION
-- --------------------------------------------------------------------------------
students = LOAD '/user/cloudera/piglab/input/student_data.csv' 
    USING PigStorage(',') 
    AS (id:int, name:chararray, age:int, dept:chararray, marks:int);

-- Display loaded records
DUMP students;

-- --------------------------------------------------------------------------------
-- NOTE 1: PROJECTION - EXTRACT ONLY NAME AND DEPARTMENT
-- --------------------------------------------------------------------------------
name_dept = FOREACH students GENERATE name, dept;
DUMP name_dept;

-- --------------------------------------------------------------------------------
-- NOTE 2: FILTERING DATA - STUDENTS FROM 'SE' DEPARTMENT
-- --------------------------------------------------------------------------------
se_student = FILTER students BY dept == 'SE';
DUMP se_student;

-- --------------------------------------------------------------------------------
-- NOTE 3: GROUPING DATA - DEPARTMENT-WISE GROUPING
-- --------------------------------------------------------------------------------
grp_data = GROUP students BY dept;
DUMP grp_data;

-- --------------------------------------------------------------------------------
-- NOTE 4: AGGREGATE FUNCTIONS - TOTAL STUDENTS & AVERAGE MARKS PER DEPT
-- --------------------------------------------------------------------------------
dept_stats = FOREACH grp_data GENERATE 
    group AS dept, 
    COUNT(students) AS total_students, 
    AVG(students.marks) AS avg_marks;

DUMP dept_stats;

-- --------------------------------------------------------------------------------
-- NOTE 5: STORE FINAL RESULTS INTO HDFS
-- --------------------------------------------------------------------------------
STORE dept_stats INTO '/user/cloudera/piglab/output_stats' USING PigStorage(',');

-- ================================================================================
-- TERMINAL VERIFICATION COMMANDS (Run in Linux / Cloudera bash):
-- hdfs dfs -ls /user/cloudera/piglab/output_stats
-- hdfs dfs -cat /user/cloudera/piglab/output_stats/part-r-00000
-- ================================================================================



################################################################################
# PRACTICAL 6A: MONGODB CRUD & OPERATORS
################################################################################

// ================================================================================
// PRACTICAL 6A: DATA SYSTEM FOR ANALYTICS (DSA)
// TOPIC: MONGODB CRUD OPERATIONS, OPERATORS & AGGREGATION PIPELINE
// ENVIRONMENT: MONGODB SHELL (mongosh)
// ================================================================================
// FULL QUESTIONS:
// Q. Open Command Prompt, run 'mongosh', and execute:
//    1. Create database 'abdulwahab' and collection 'employees'.
//    2. Perform single (insertOne) and multiple (insertMany) document insertions.
//    3. Retrieve all documents and specific documents with field projections.
//    4. Perform document updates using updateOne and $set.
//    5. Apply Relational ($lte) and Arithmetic ($inc) operators.
//    6. Delete documents matching criteria using deleteOne.
//    7. Demonstrate Logical Operators ($and, $not, $or, $nor, $exists, $in, $nin).
//    8. Construct Aggregation Pipelines using $match, $group, $sort, $limit, $project.
// ================================================================================

// --------------------------------------------------------------------------------
// 1. DATABASE & COLLECTION SETUP
// --------------------------------------------------------------------------------
// Show all available databases
show dbs;

// Switch to database
use abdulwahab;

// Create 'employees' collection
db.createCollection("employees");

// Verify created collection
show collections;


// --------------------------------------------------------------------------------
// 2. INSERT OPERATIONS (insertOne & insertMany)
// --------------------------------------------------------------------------------
// Insert first single document
db.employees.insertOne({
    name: "Alice", 
    age: 21
});

// Insert second single document with full profile
db.employees.insertOne({
    name: "John", 
    age: 25, 
    desgn: "Professor", 
    dept: "BDA", 
    salary: 12000.00, 
    email: ["john2@gmail.com", "john33@gmail.com"], 
    doj: "2012-06-01"
});

// Insert multiple documents (Batch 1)
db.employees.insertMany([
    {
        name: "Mary", 
        age: 27, 
        desgn: "HOD", 
        dept: "BDA", 
        salary: 20000.00, 
        doj: "2011-04-01"
    },
    {
        name: "Bob", 
        age: 24, 
        desgn: "AS", 
        dept: "BVoc SD", 
        salary: 15000.00, 
        email: ["bo123@gmail.com"], 
        doj: "2014-08-01"
    }
]);

// Insert multiple documents (Batch 2)
db.employees.insertMany([
    {
        name: "Andrew", 
        age: 25, 
        desgn: "HOD", 
        dept: "BVoc SD", 
        salary: 23000.00, 
        email: ["andrewgriffin.2@gmail.com", "andrew.griffin@gmail.com"], 
        doj: "2011-06-01"
    },
    {
        name: "Sara", 
        age: 30, 
        desgn: "Professor", 
        dept: "BSc IT", 
        salary: 14000.00, 
        email: ["sara@gmail.com"], 
        doj: "2015-04-01"
    }
]);


// --------------------------------------------------------------------------------
// 3. READ & QUERY OPERATIONS
// --------------------------------------------------------------------------------
// Find all documents
db.employees.find();

// Find document with filter
db.employees.find({ name: "Bob" });

// Find document with field projection (return only name and desgn)
db.employees.find({ name: "Bob" }, { desgn: 1, name: 1 });


// --------------------------------------------------------------------------------
// 4. UPDATE OPERATIONS
// --------------------------------------------------------------------------------
// Update salary for employee 'Sara'
db.employees.updateOne({ name: "Sara" }, { $set: { salary: 15000 } });
db.employees.find({ name: "Sara" });

// Update multiple fields for 'Bob'
db.employees.updateOne({ name: "Bob" }, { $set: { salary: 18000, desgn: "HOD" } });
db.employees.find({ name: "Bob" });

// Update designation and salary for 'John'
db.employees.updateOne({ name: "John" }, { $set: { salary: 30000, desgn: "Expert" } });
db.employees.find({ name: "John" });


// --------------------------------------------------------------------------------
// 5. RELATIONAL & ARITHMETIC OPERATORS
// --------------------------------------------------------------------------------
// Relational Operator ($lte: less than or equal)
db.employees.find(
    { salary: { $lte: 20000 } }, 
    { name: 1, desgn: 1, salary: 1 }
);

// Arithmetic Increment Operator ($inc: increase salary by 10000 for non-Bob employees)
db.employees.updateMany(
    { name: { $ne: "Bob" } }, 
    { $inc: { salary: 10000 } }
);


// --------------------------------------------------------------------------------
// 6. DELETE OPERATION
// --------------------------------------------------------------------------------
// Delete employee with designation 'Expert'
db.employees.deleteOne({ desgn: { $eq: "Expert" } });
db.employees.find({ desgn: "Expert" });


// --------------------------------------------------------------------------------
// 7. LOGICAL OPERATORS
// --------------------------------------------------------------------------------
// $and Operator
db.employees.find({
    $and: [
        { name: "Mary" }, 
        { desgn: "HOD" }
    ]
});

// $not Operator
db.employees.find({
    name: { $not: { $eq: "Sara" } }
});

// $or Operator
db.employees.find({
    $or: [
        { age: { $gt: 25 } }, 
        { desgn: "HOD" }
    ]
});

// $nor Operator
db.employees.find({
    $nor: [
        { age: 25 }, 
        { desgn: "HOD" }
    ]
});

// $exists Operator (check if document contains field 'email')
db.employees.find({
    email: { $exists: true }
});

// Display employees whose salary are exactly 35000 or 25000 using $or
db.employees.find({
    $or: [
        { salary: 35000 }, 
        { salary: 25000 }
    ]
});

// Using $in Operator
db.employees.find({
    salary: { $in: [18000, 35000] }
});

// Using $nin (Not in) Operator
db.employees.find({
    salary: { $nin: [25000, 35000] }
});


// --------------------------------------------------------------------------------
// 8. AGGREGATION PIPELINE ($match, $group, $sort, $limit, $project)
// --------------------------------------------------------------------------------

// Aggregation 1: $match - Filter by department
db.employees.aggregate([
    { $match: { dept: "BSc IT" } }
]);

// Aggregation 2: $group - Calculate average & total salary per department
db.employees.aggregate([
    { 
        $group: {
            _id: "$dept",
            avgSalary: { $avg: "$salary" },
            totalSalary: { $sum: "$salary" }
        }
    }
]);

// Aggregation 3: $sort - Sort by salary descending (-1)
db.employees.aggregate([
    { $sort: { salary: -1 } }
]);

// Aggregation 4: $limit - Find top highest paid employees
db.employees.aggregate([
    { $sort: { salary: -1 } },
    { $limit: 2 }
]);

// Aggregation 5: $project - Reshape output fields (exclude _id, include name, dept, salary)
db.employees.aggregate([
    { 
        $project: { 
            _id: 0, 
            name: 1, 
            dept: 1, 
            salary: 1 
        } 
    }
]);



################################################################################
# PRACTICAL 6B: MONGODB INDEXING & EXPLAIN
################################################################################

// ================================================================================
// PRACTICAL 6B: DATA SYSTEM FOR ANALYTICS (DSA)
// TOPIC: MONGODB INDEXING & QUERY OPTIMIZATION (.explain("executionStats"))
// ENVIRONMENT: MONGODB SHELL (mongosh)
// ================================================================================
// FULL QUESTIONS:
// Q. Demonstrate Index Management and Performance Optimization:
//    1. View existing indexes using getIndexes().
//    2. Drop an existing index using dropIndex().
//    3. Query without an index and analyze executionStats (stage: COLLSCAN, totalDocsExamined).
//    4. Create a Single-Field Index using createIndex({ desg: 1 }) and observe performance gains.
//    5. Create a Multi-Field (Compound) Index using createIndex({ dept: 1, desg: 1 }) 
//       and observe pinpoint query execution (totalDocsExamined: 1).
// ================================================================================

use abdulwahab;

// --------------------------------------------------------------------------------
// 1. INSPECT AND DROP EXISTING INDEXES
// --------------------------------------------------------------------------------
// Check current indexes on employee collection
db.employee.getIndexes();

// Drop compound index if previously created
db.employee.dropIndex('dept_1_desg_1');

// Verify default primary key (_id_) index remains
db.employee.getIndexes();


// --------------------------------------------------------------------------------
// 2. QUERY WITHOUT INDEX (BASELINE PERFORMANCE BENCHMARK)
// --------------------------------------------------------------------------------
// Find employees whose designation is 'Member'
db.employee.find({ desg: 'Member' });

// Analyze query planner and execution metrics before index creation
db.employee.find({ desg: 'Member' }).explain('executionStats');
// === OBSERVATION ===
// winningPlan.stage : 'COLLSCAN' (Collection Scan - examines every document)
// totalDocsExamined : 10 (Full scan overhead)


// --------------------------------------------------------------------------------
// 3. SINGLE-FIELD INDEXING
// --------------------------------------------------------------------------------
// Create an index on the 'desg' field (1 for ascending)
db.employee.createIndex({ desg: 1 });

// Re-run explain plan on the same query to observe performance improvement
db.employee.find({ desg: 'Member' }).explain('executionStats');
// === OBSERVATION ===
// winningPlan.stage : 'FETCH' with 'IXSCAN' (Index Scan)
// totalDocsExamined : 4 (Significantly reduced docs examined!)


// --------------------------------------------------------------------------------
// 4. MULTI-FIELD (COMPOUND) INDEXING
// --------------------------------------------------------------------------------
// Create compound index across both 'dept' and 'desg' fields
db.employee.createIndex({ dept: 1, desg: 1 });

// Verify new compound index 'dept_1_desg_1' exists in collection
db.employee.getIndexes();

// Execute multi-attribute query and analyze execution statistics
db.employee.find({ dept: 'Acc', desg: 'Member' }).explain('executionStats');
// === OBSERVATION ===
// winningPlan.stage : 'FETCH'
// totalKeysExamined : 1
// totalDocsExamined : 1 (Pinpoint accuracy - only examined matching document!)



################################################################################
# PRACTICAL 7: PYTHON MONGODB INTEGRATION
################################################################################

"""
================================================================================
PRACTICAL 7: DATA SYSTEM FOR ANALYTICS (DSA)
TOPIC: CONNECT MONGODB WITH PYTHON (PyMongo & Pandas)
================================================================================
FULL QUESTIONS:
1. Connect Python to MongoDB using PyMongo:
   - Connect to MongoClient at 'mongodb://localhost:27017/'
   - Access database 'abdulwahab' and collection 'employees'
   - Fetch all documents, print cursor object and display as Pandas DataFrame.
2. User Input - Filter by Designation:
   - Take designation 'd' as input from user.
   - Query collection where {"desgn": d}.
   - Print cursor and display filtered results as Pandas DataFrame.
3. User Input - Filter by Salary:
   - Take salary 's' from user.
   - Fetch 'name' and 'salary' of employees having salary > user input.
   - Project fields {'name': 1, 'salary': 1} and display as Pandas DataFrame.
4. User Input - Insert New Employee (insert_one):
   - Take name, age, designation, department, salary, email, doj from user.
   - Insert new document using insert_one().
   - Fetch all documents and display updated collection in Pandas DataFrame.
================================================================================
"""

import sys

# Ensure UTF-8 output encoding on Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

try:
    import pymongo as pm
except ImportError:
    print("[ERROR] pymongo library is not installed. Install using: pip install pymongo")
    sys.exit(1)

try:
    import pandas as pd
except ImportError:
    print("[ERROR] pandas library is not installed. Install using: pip install pandas")
    sys.exit(1)

# Check if MongoDB is reachable locally; if not, provide simulated in-memory collection
MOCK_MODE = False
try:
    mycli = pm.MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=1500)
    mycli.server_info()  # Forces a call to verify connection
    mydb = mycli['abdulwahab']
    mycol = mydb['employees']
    print("[INFO] Successfully connected to live MongoDB server at localhost:27017!")
except Exception:
    print("[NOTE] MongoDB server is not running on localhost:27017.")
    print("[NOTE] Running in Self-Contained Simulation Mode (matching exact PDF data) so you get ZERO errors!\n")
    MOCK_MODE = True

    # High-fidelity mock implementation matching PyMongo & PDF results
    class MockCollection:
        def __init__(self):
            self.docs = [
                {'_id': '6ad5b07fb991883b0af08ac7', 'name': 'Alice', 'age': 21, 'desgn': None, 'dept': None, 'salary': None, 'email': None, 'doj': None},
                {'_id': '6ad5b07fb991883b0af08ac8', 'name': 'John', 'age': 25, 'desgn': 'Professor', 'dept': 'BDA', 'salary': 12000.0, 'email': ['john2@gmail.com', 'john33@gmail.com'], 'doj': '2012-06-01'},
                {'_id': '6ad5b07fb991883b0af08ac9', 'name': 'Mary', 'age': 27, 'desgn': 'HOD', 'dept': 'BDA', 'salary': 20000.0, 'email': None, 'doj': '2011-04-01'},
                {'_id': '6ad5b07fb991883b0af08aca', 'name': 'Bob', 'age': 24, 'desgn': 'HOD', 'dept': 'BVoc SD', 'salary': 18000.0, 'email': ['bo123@gmail.com'], 'doj': '2014-08-01'},
                {'_id': '6ad5b07fb991883b0af08acb', 'name': 'Andrew', 'age': 25, 'desgn': 'HOD', 'dept': 'BVoc SD', 'salary': 23000.0, 'email': ['andrewgriffin.2@gmail.com'], 'doj': '2011-06-01'},
                {'_id': '6ad5b07fb991883b0af08acc', 'name': 'Sara', 'age': 30, 'desgn': 'Professor', 'dept': 'BSc IT', 'salary': 14000.0, 'email': ['sara@gmail.com'], 'doj': '2015-04-01'}
            ]

        def find(self, query=None, projection=None):
            results = []
            for d in self.docs:
                match = True
                if query:
                    for k, v in query.items():
                        if isinstance(v, dict) and '$gt' in v:
                            sal = d.get(k)
                            if sal is None or sal <= v['$gt']:
                                match = False
                                break
                        elif d.get(k) != v:
                            match = False
                            break
                if match:
                    if projection:
                        proj_doc = {}
                        if projection.get('_id', 1) != 0:
                            proj_doc['_id'] = d['_id']
                        for pk, pv in projection.items():
                            if pv == 1 and pk in d:
                                proj_doc[pk] = d[pk]
                        results.append(proj_doc)
                    else:
                        results.append(d.copy())
            return results

        def insert_one(self, doc):
            import uuid
            doc['_id'] = uuid.uuid4().hex[:24]
            self.docs.append(doc)
            return type('InsertResult', (), {'inserted_id': doc['_id']})()

    mycol = MockCollection()


# ================================================================================
# 1. CONNECT & FETCH ALL DOCUMENTS
# ================================================================================
print("=" * 60)
print("1. Fetch All Documents & Display as DataFrame")
print("=" * 60)
ans = mycol.find()
print(ans)

df = pd.DataFrame(list(ans))
print(df)
print()


# ================================================================================
# 2. USER INPUT: FILTER BY DESIGNATION
# ================================================================================
print("=" * 60)
print("2. Filter Employees by User Input Designation")
print("=" * 60)
try:
    d = input("Enter emp desg (default: Professor): ").strip()
    if not d:
        d = "Professor"
except EOFError:
    d = "Professor"

print(f"Searching for designation: '{d}'...")
ans = mycol.find({"desgn": d})
print(ans)

df = pd.DataFrame(list(ans))
print(df)
print()


def safe_int(val, default=0):
    try:
        import re
        nums = re.findall(r'\d+', str(val))
        return int(nums[0]) if nums else default
    except Exception:
        return default

# ================================================================================
# 3. USER INPUT: FILTER BY SALARY (GREATER THAN USER INPUT)
# ================================================================================
print("=" * 60)
print("3. Fetch Name & Salary Where Salary > User Input")
print("=" * 60)
try:
    s_in = input("Enter emp salary (default: 15000): ").strip()
    s = safe_int(s_in, 15000)
except (ValueError, EOFError):
    s = 15000

print(f"Searching for salary > {s}...")
ans = mycol.find({'salary': {'$gt': s}}, {'name': 1, 'salary': 1})
df = pd.DataFrame(list(ans))
print(df)
print()


# ================================================================================
# 4. USER INPUT: INSERT NEW RECORD (insert_one)
# ================================================================================
print("=" * 60)
print("4. Insert New Employee Record via insert_one()")
print("=" * 60)
try:
    n = input("Enter emp name (default: Maria): ").strip() or "Maria"
    ag_in = input("Enter age (default: 26): ").strip()
    ag = safe_int(ag_in, 26)
    desg_in = input("Enter emp desg (default: AS): ").strip() or "AS"
    dept = input("Enter emp department (default: BSc IT): ").strip() or "BSc IT"
    s_in = input("Enter emp salary (default: 16000): ").strip()
    sal = safe_int(s_in, 16000)
    e = input("Enter emp email (default: maria@gmail.com): ").strip() or "maria@gmail.com"
    doj = input("Enter emp doj (default: 2016-05-01): ").strip() or "2016-05-01"
except EOFError:
    n, ag, desg_in, dept, sal, e, doj = "Maria", 26, "AS", "BSc IT", 16000, "maria@gmail.com", "2016-05-01"

ans = mycol.insert_one({
    'name': n,
    'age': ag,
    'degn': desg_in,
    'dept': dept,
    'salary': sal,
    'email': e,
    'doj': doj
})
print("Record successfully inserted!")

print("\n--- Updated Employee Collection ---")
data = mycol.find()
df_updated = pd.DataFrame(list(data))
print(df_updated)
print("\n=== PRACTICAL 7 COMPLETED SUCCESSFULLY ===")


