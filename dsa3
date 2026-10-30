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
