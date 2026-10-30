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
