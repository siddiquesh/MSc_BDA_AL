"""
================================================================================
PRACTICAL 1: DESCRIPTIVE STATISTICS & EXPLORATORY DATA ANALYSIS (EDA)
================================================================================
FULL QUESTIONS:

Q1) Analyze the Iris Dataset:
    1. Load the Iris Dataset (150 rows, 4 numerical features).
    2. Calculate Mean, Median, Mode(s), Standard Deviation, Variance, Skewness, Kurtosis
       for each numerical feature.
    3. Plot distribution histograms with KDE for all numerical features.
    4. Provide detailed feature-by-feature statistical interpretation.

Q2) Analyze the Tips Dataset:
    1. Load the Tips Dataset (244 rows, 7 columns).
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for numerical features (total_bill, tip, size).
    3. Plot histograms with KDE for numerical features.
    4. Provide statistical interpretation of customer billing & tipping behavior.

Q3) Analyze the Indian Stock Market Dataset:
    1. Load 'indian_stock_market.csv' (2306 rows).
    2. Calculate summary statistics for numerical stock prices (MSFT, IBM, SBUX, AAPL, GSPC).
    3. Plot distribution histograms with KDE in a 3x2 grid.
================================================================================
"""

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Q1: Iris Dataset
# ------------------------------------------------------------------------------
iris = sns.load_dataset('iris')
print("--- Iris Dataset Head ---")
print(iris.head())
print("
--- Iris Dataset Info ---")
iris.info()

numerical_cols = iris.select_dtypes(include=np.number).columns.tolist()

for col in numerical_cols:
    mean_val = iris[col].mean()
    median_val = iris[col].median()
    mode_val = iris[col].mode().tolist() # mode() can return multiple values
    std_val = iris[col].std()
    var_val = iris[col].var()
    skewness_val = skew(iris[col])
    kurtosis_val = kurtosis(iris[col])
    print(f"... Statistics for '{col}'")
    print(f" Mean: {mean_val:.3f}")
    print(f" Median: {median_val:.3f}")
    print(f" Mode: {mode_val}")
    print(f" Standard Deviation: {std_val:.3f}")
    print(f" Variance: {var_val:.3f}")
    print(f" Skewness: {skewness_val:.3f}")
    print(f" Kurtosis: {kurtosis_val:.3f}")
    print("
")

"""
Q1 Interpretation:
1. General Dataset Overview: 150 entries, no missing values, 4 numerical features and 1 categorical species.
2. Sepal Length: Mean (5.843) and Median (5.800) are very close. Slight positive skewness (0.315) pulls the mean slightly higher.
3. Sepal Width: Mean (3.057) and Median (3.000) closely approximate a standard normal distribution.
4. Petal Length (Bimodal): Gap between mean (3.758) and median (4.350). Two modes (1.4 and 1.5). High negative kurtosis (-1.402) confirms a bimodal distribution due to Setosa clustering at 1.4-1.5 while other species cluster higher.
5. Petal Width: Mode at low end (0.2) represents small Setosa petals, while median (1.3) reflects larger flowers.
"""

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 2, i + 1)
    sns.histplot(iris[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Q2: Tips Dataset
# ------------------------------------------------------------------------------
tips = sns.load_dataset('tips')
print("--- Tips Dataset Head ---")
print(tips.head())
tips.info()

numerical_cols = tips.select_dtypes(include=np.number).columns.to_list()

for col in numerical_cols:
    mean_val = tips[col].mean()
    median_val = tips[col].median()
    mode_val = tips[col].mode().tolist()
    std_val = tips[col].std()
    var_val = tips[col].var()
    skew_val = skew(tips[col])
    kurtosis_val = kurtosis(tips[col])

    print(f"----- Stats for '{col}' -----")
    print(f"Mean: {mean_val:.3f}")
    print(f"Median: {median_val:.3f}")
    print(f"Mode: {mode_val}")
    print(f"Standard Deviation: {std_val:.3f}")
    print(f"Variance: {var_val:.3f}")
    print(f"Skewness: {skew_val:.3f}")
    print(f"Kurtosis: {kurtosis_val:.3f}
")

"""
Q2 Interpretation:
1. Total Bill: Right-skewed distribution (skewness 1.133). Most bills are small, but high-end bills pull the mean (19.786) above the median (17.795).
2. Tip: High kurtosis (3.648) shows concentration around $2-$3, with a round-number mode of exactly $2.00.
3. Party Size: Discrete integers peaking at parties of two (mode = 2, median = 2).
"""

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 2, i + 1)
    sns.histplot(tips[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Q3: Indian Stock Market Dataset
# ------------------------------------------------------------------------------
df = pd.read_csv('indian_stock_market.csv')

numerical_cols = df.select_dtypes(include=np.number).columns.to_list()

for col in numerical_cols:
    mean_val = df[col].mean()
    median_val = df[col].median()
    mode_val = df[col].mode().tolist()
    std_val = df[col].std()
    var_val = df[col].var()
    skew_val = skew(df[col].dropna(), nan_policy='omit')
    kurtosis_val = kurtosis(df[col].dropna(), nan_policy='omit')

    print(f"----- Stats for '{col}' -----")
    print(f"Mean: {mean_val:.3f}")
    print(f"Median: {median_val:.3f}")
    print(f"Mode: {mode_val}")
    print(f"Standard Deviation: {std_val:.3f}")
    print(f"Variance: {var_val:.3f}")
    print(f"Skewness: {skew_val:.3f}")
    print(f"Kurtosis: {kurtosis_val:.3f}
")

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(3, 2, i + 1)
    sns.histplot(df[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
