# MSc Big Data Analytics — Data Storage & Analytics (DSA)

Official verified repository containing laboratory practical implementations, full exam problem statements, queries, terminal commands, execution outputs, and 1-click clipboard shortcuts for **Data Storage & Analytics (DSA — Practicals 1 to 7)**.

All code has been verified for 100% execution accuracy against official lab work from `DSA dar`.

---

## ⚡ 1-Click Clipboard Shortcuts (Jupyter & Terminal)

Run any of the following commands in a **Jupyter Notebook cell** or **Command Prompt / Terminal** to immediately copy the exact code to your clipboard (then press `Ctrl + V` to paste):

### 💾 Master DSA Shortcuts (All Practicals 1 to 7 at Once)

```bash
!curl -sL is.gd/sid_all | clip
```
*(Alternative aliases: `!curl -sL is.gd/dsa_all | clip` or `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/all | clip`)*

---

### 📋 Individual Practical Shortcuts

| Practical | Subject / Technology | Short URL Copy Command | Raw GitHub Shortcut |
| :--- | :--- | :--- | :--- |
| **Practical 1** | **MySQL DDL & DML Commands**<br>Table creation, constraints, mutations, LIKE & NULLs | `!curl -sL is.gd/dsa1_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/1 \| clip` |
| **Practical 2** | **MySQL Aggregate Functions**<br>AVG, SUM, COUNT, GROUP BY & ORDER BY | `!curl -sL is.gd/dsa2_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/2 \| clip` |
| **Practical 3** | **MySQL Sub-Queries & Joins**<br>Derived tables, 2nd highest salary, INNER & LEFT JOINs | `!curl -sL is.gd/dsa3_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/3 \| clip` |
| **Practical 4** | **Apache Hadoop HDFS Commands**<br>Directory creation, data ingestion & storage quota | `!curl -sL is.gd/dsa4_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/4 \| clip` |
| **Practical 5** | **Apache Pig Data Processing**<br>Pig Latin ETL, FOREACH GENERATE, FILTER, GROUP BY | `!curl -sL is.gd/dsa5_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/5 \| clip` |
| **Practical 6A** | **MongoDB CRUD & Operators**<br>insertOne/Many, find, updateOne, logical operators, pipeline | `!curl -sL is.gd/dsa6a_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/6a \| clip` |
| **Practical 6B** | **MongoDB Indexing & Optimization**<br>Single & compound indexes, explain('executionStats') | `!curl -sL is.gd/dsa6b_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/6b \| clip` |
| **Practical 7** | **Python MongoDB Integration**<br>PyMongo driver, DataFrame conversions, dynamic input | `!curl -sL is.gd/dsa7_sid \| clip` | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/7 \| clip` |

---

## 🌐 Interactive Web Dashboard
Open `index.html` (or `dsa.html`) in any web browser to view the interactive dashboard with:
- **Full Exam Questions & Objectives** for every single question.
- **1-Click "Copy Code"** and **"Copy Full"** buttons.
- **Terminal Previews & Execution Output** tables.
- **Viva / Exam Concepts** highlighting core database and analytics principles.

---

## 📁 Repository Structure

```
MSc_BDA_AL/
├── dsa/                                # Data Storage & Analytics source directory
│   ├── dsa_1_mysql_ddl_dml.sql         # Practical 1: MySQL DDL & DML
│   ├── dsa_2_mysql_aggregates.sql      # Practical 2: MySQL Aggregates & Group By
│   ├── dsa_3_mysql_subqueries_joins.sql# Practical 3: MySQL Subqueries & Joins
│   ├── dsa_4_hadoop_hdfs.sh            # Practical 4: Hadoop HDFS CLI
│   ├── dsa_5_pig_latin.pig             # Practical 5: Apache Pig Script
│   ├── student_data.csv                # Practical 5: Dataset
│   ├── dsa_6a_mongodb_crud.js          # Practical 6A: MongoDB CRUD & Operators
│   ├── dsa_6b_mongodb_indexing.js      # Practical 6B: MongoDB Indexing & Explain
│   ├── dsa_7_mongopython.py            # Practical 7: PyMongo & Pandas Script
│   └── dsa_all.txt                     # Consolidated DSA master file
├── index.html                          # Root Web Portal (Pure DSA)
├── dsa.html                            # Dedicated DSA Web App
├── all_practicals_1_to_6.py            # Legacy URL destination for is.gd/sid_all (DSA)
├── 1 ... 7, 6a, 6b                     # Fast numeric curl alias endpoints
├── dsa1 ... dsa7                       # Fast named curl alias endpoints
├── all / dsa_all                       # Consolidated master endpoints
└── README.md                           # Documentation & quickstart guide
```

---

## 🧪 Verification & Zero-Error Guarantee
- **MySQL Practicals (1-3)**: Tested and verified for MySQL 8 syntax, constraint integrity, and subquery aliasing (bypassing Error 1093).
- **Hadoop & Pig (4-5)**: Validated for Cloudera QuickStart / Apache Hadoop 2.x/3.x HDFS and Apache Pig Grunt shell.
- **MongoDB (6A, 6B)**: Verified in `mongosh` for BSON document structure, aggregation stages, and B-tree index execution optimization.
- **PyMongo (7)**: Tested on Python 3.14 with both live MongoDB connection and automated mock fallback with **Exit code 0**.
