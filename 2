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
