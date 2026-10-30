# MSc Big Data Analytics — Practicals Suite (ASM & DSA)

Official verified repository containing laboratory practical implementations, full exam questions, terminal commands, execution outputs, and 1-click clipboard web applications for:
1. **Applied Statistical Methods (ASM) — Practicals 1 to 9**
2. **Data Storage & Analytics (DSA) — Practicals 1 to 7**

All code has been verified for 100% execution accuracy against official lab work from `ASM Dar` and `DSA dar`.

---

## ⚡ 1-Click Clipboard Shortcuts (Jupyter & Terminal)

Run any of the following commands in a **Jupyter Notebook cell** or **Command Prompt / Bash** to immediately copy the exact code to your clipboard:

### 📊 Applied Statistical Methods (ASM) Shortcuts

| Practical | Subject / Topic | Jupyter Cell Copy Command |
| :--- | :--- | :--- |
| **All ASM (1-9)** | Complete Suite (Practicals 1 to 9) | `!curl -sL is.gd/sid_all \| clip` |
| **Practical 1** | Descriptive Statistics & Exploratory Data Analysis (EDA) | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm1 \| clip` |
| **Practical 2** | Probability Distributions (Normal, Binomial, Poisson) | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm2 \| clip` |
| **Practical 3** | Confidence Intervals & Empirical Bootstrapping | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm3 \| clip` |
| **Practical 4** | Hypothesis Testing (t-test, Chi-Square, ANOVA & Tukey HSD) | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm4 \| clip` |
| **Practical 5** | A/B Testing Analysis (Two-Sample t-test & Proportions z-test) | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm5 \| clip` |
| **Practical 6** | Linear Regression & Spearman Rank Correlation | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm6 \| clip` |
| **Practical 7** | Logistic Regression & Multi-Metric Evaluation | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm7 \| clip` |
| **Practical 8** | Principal Component Analysis (PCA) & Variance Explained | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm8 \| clip` |
| **Practical 9** | Bayesian Updating for Medical Diagnostic Testing | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/asm9 \| clip` |

---

### 💾 Data Storage & Analytics (DSA) Shortcuts

| Practical | Subject / Technology | Terminal / CLI Copy Command |
| :--- | :--- | :--- |
| **All DSA (1-7)** | Complete Suite (Practicals 1 to 7) | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa_all \| clip` |
| **Practical 1** | MySQL DDL & DML Commands, Constraints, LIKE & NULLs | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa1 \| clip` |
| **Practical 2** | MySQL Aggregate Functions, GROUP BY & ORDER BY | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa2 \| clip` |
| **Practical 3** | MySQL Sub-Queries, Derived Tables, INNER & LEFT JOINs | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa3 \| clip` |
| **Practical 4** | Apache Hadoop HDFS Commands & Ingestion | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa4 \| clip` |
| **Practical 5** | Apache Pig Latin Data Processing & HDFS Storage | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa5 \| clip` |
| **Practical 6A** | MongoDB CRUD, Relational/Logical Operators & Pipeline | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa6a \| clip` |
| **Practical 6B** | MongoDB Indexing & Query Optimization (`explain`) | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa6b \| clip` |
| **Practical 7** | Connecting MongoDB with Python (PyMongo & Pandas) | `!curl -sL https://raw.githubusercontent.com/siddiquesh/MSc_BDA_AL/main/dsa7 \| clip` |

---

## 🌐 Interactive Web Portals

- **ASM Dashboard (`index.html` / `asm.html`)**: Sleek dark neon theme featuring all 9 statistical practicals with full exam problem statements, code blocks, terminal outputs, and 1-click copy buttons.
- **DSA Dashboard (`dsa.html`)**: Interactive dashboard featuring all 7 data storage practicals covering MySQL, Hadoop, Pig Latin, MongoDB, and Python database integration.

---

## 📁 Repository Structure

```
MSc_BDA_AL/
├── asm/                                # Applied Statistical Methods directory
│   ├── practical_1.py ... practical_9.py
│   └── asm_all.py
├── dsa/                                # Data Storage & Analytics directory
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
├── index.html                          # Root Web Portal (ASM with switcher)
├── asm.html                            # Dedicated ASM Dashboard
├── dsa.html                            # Dedicated DSA Dashboard
├── asm1 ... asm9                       # Fast curl alias endpoints for ASM
├── dsa1 ... dsa7                       # Fast curl alias endpoints for DSA
└── README.md                           # Documentation & quickstart guide
```

---

## 🧪 Verification & Testing Guarantee

- **ASM Practicals (1-9)**: Executed and verified using Python 3.14 with 100% exit code 0.
- **DSA Practicals (1-7)**: Verified against MySQL 8, Hadoop 2.x/3.x HDFS, Apache Pig, MongoDB 6/7, and Python 3.14 PyMongo with zero syntax errors.
