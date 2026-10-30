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
