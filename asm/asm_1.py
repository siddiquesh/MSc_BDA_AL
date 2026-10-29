"""
================================================================================
PRACTICAL 1: DESCRIPTIVE STATISTICS & EXPLORATORY DATA ANALYSIS (EDA)
================================================================================
FULL QUESTIONS:

Q1) Analyze the Iris Dataset:
    1. Load the Iris Dataset.
    2. Calculate mean of each numerical feature.
    3. Calculate median of each numerical feature.
    4. Calculate mode(s) of each numerical feature.
       (Note: Mode can be multi-modal or cannot be calculated for continuous data)
    5. Calculate standard deviation of each numerical feature.
    6. Calculate variance of each numerical feature.
    7. Calculate skewness of each numerical feature.
    8. Calculate kurtosis of each numerical feature.
    9. Plot the distribution (histogram with KDE) for each numerical feature.
    10. Interpret the results.

Q2) Analyze the Tips Dataset:
    1. Load the Tips Dataset.
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for all numerical features (total_bill, tip, size).
    3. Plot histograms with KDE for numerical features.
    4. Interpret the results.

Q3) Analyze the Indian Stock Market Dataset:
    1. Load 'indian_stock_market.csv'.
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for numerical stock prices (MSFT, IBM, SBUX, AAPL, GSPC).
    3. Plot distribution histograms with KDE.
    4. Interpret the results.
================================================================================
"""

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew,kurtosis
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())
iris.info()

numerical_cols = iris.select_dtypes(include=np.number).columns.to_list()
for col in numerical_cols:
  mean_val = iris[col].mean()
  median_val = iris[col].median()
  mode_val = iris[col].mode().tolist()
  std_val = iris[col].std()
  var_val = iris[col].var()
  skewness_val = skew(iris[col])
  kurtosis_val = kurtosis(iris[col])
  print(f"---Stats for {col}---")
  print(f" Mean: {mean_val}")
  print(f" Median: {median_val}")
  print(f" Mode: {mode_val}")
  print(f" Standard Deviation: {std_val}")
  print(f" Variance: {var_val}")
  print(f" Skewness: {skewness_val}")
  print(f" Kurtosis: {kurtosis_val}")
  print("\n")

plt.figure(figsize=(15,10))
for i, col in enumerate(numerical_cols):
  plt.subplot(2,2,i+1)
  sns.histplot(iris[col],kde=True,bins=15)
  plt.title(f'Distribution of {col}')
  plt.xlabel('col')
  plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Q2) Analyze the Tips dataset

tips = sns.load_dataset('tips')
print(tips.head())
tips.info()

numerical_cols = tips.select_dtypes(include=np.number).columns.to_list()
for col in numerical_cols:
  mean_val = tips[col].mean()
  median_val = tips[col].median()
  mode_val = tips[col].mode().tolist()
  std_val = tips[col].std()
  var_val = tips[col].var()
  skewness_val = skew(tips[col])
  kurtosis_val = kurtosis(tips[col])
  print(f"---Stats for {col}---")
  print(f" Mean: {mean_val}")
  print(f" Median: {median_val}")
  print(f" Mode: {mode_val}")
  print(f" Standard Deviation: {std_val}")
  print(f" Variance: {var_val}")
  print(f" Skewness: {skewness_val}")
  print(f" Kurtosis: {kurtosis_val}")
  print("\n")

plt.figure(figsize=(15,10))
for i, col in enumerate(numerical_cols):
  plt.subplot(2,2,i+1)
  sns.histplot(tips[col],kde=True,bins=15)
  plt.title(f'Distribution of {col}')
  plt.xlabel('col')
  plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Q3) Analyze the Stock dataset

import pandas as pd
stock = pd.read_csv('indian_stock_market.csv')
print(stock.head())
stock.info()

numerical_cols = stock.select_dtypes(include=np.number).columns.to_list()
for col in numerical_cols:
  mean_val = stock[col].mean()
  median_val = stock[col].median()
  mode_val = stock[col].mode().tolist()
  std_val = stock[col].std()
  var_val = stock[col].var()
  skewness_val = skew(stock[col])
  kurtosis_val = kurtosis(stock[col])
  print(f"---Stats for {col}---")
  print(f" Mean: {mean_val}")
  print(f" Median: {median_val}")
  print(f" Mode: {mode_val}")
  print(f" Standard Deviation: {std_val}")
  print(f" Variance: {var_val}")
  print(f" Skewness: {skewness_val}")
  print(f" Kurtosis: {kurtosis_val}")
  print("\n")

plt.figure(figsize=(15, 15))
for i, col in enumerate(numerical_cols):
   plt.subplot(3, 2, i + 1)
   sns.histplot(stock[col], kde=True, bins=15)
   plt.title(f'Distribution of {col}')
   plt.xlabel(col)
   plt.ylabel('Frequency')
plt.tight_layout()
plt.show()