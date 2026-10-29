# ASM Practical 6 - Linear Regression & Correlation

# Question 1: Simple Linear Regression (Diabetes Dataset)
from sklearn.datasets import load_diabetes
import pandas as pd
import statsmodels.api as sm

diabetes = load_diabetes(as_frame=True)
df = diabetes.frame
print(df.head())

# correlation
print(df[["bmi", "target"]].corr())

# Simple linear regression
X = sm.add_constant(df["bmi"])
y = df['target']
model = sm.OLS(y, X).fit()
print(model.summary())

# Question 2: Multiple Linear Regression
X = df[["bmi", "bp", "age"]]
X = sm.add_constant(X)
model = sm.OLS(df["target"], X).fit()
print(model.summary())

# Question 3: Spearman Rank Correlation
from scipy.stats import spearmanr

study_time = [2, 4, 1, 5, 3]
exam_score = [50, 65, 45, 80, 60]

correlation, p_value = spearmanr(study_time, exam_score)
print("Spearman Correlation:", correlation)
print("P-value:", p_value)
