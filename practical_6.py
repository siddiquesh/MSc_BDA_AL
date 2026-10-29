"""
================================================================================
PRACTICAL 6: LINEAR REGRESSION & CORRELATION
================================================================================
FULL QUESTIONS:

Question 1: (Simple Linear Regression)
    Load the scikit-learn Diabetes dataset into a pandas DataFrame.
    1. Evaluate the Pearson correlation between Body Mass Index ('bmi') and the
       disease progression outcome ('target').
    2. Fit an Ordinary Least Squares (OLS) Simple Linear Regression model
       (target ~ bmi + intercept) using statsmodels.
    3. Output and interpret the model summary (R-squared, coefficients, p-values).

Question 2: (Multiple Linear Regression)
    Fit an OLS Multiple Linear Regression model predicting disease progression ('target')
    using three predictors: 'bmi', blood pressure ('bp'), and 'age'.
    Add an intercept constant and evaluate:
    - Overall model fit (R-squared, F-statistic).
    - Which individual variables are statistically significant predictors.

Question 3: (Spearman Rank Correlation)
    Given:
    study_time = [2, 4, 1, 5, 3]
    exam_score = [50, 65, 45, 80, 60]
    Calculate the Spearman rank correlation coefficient and p-value.
    Interpret the monotonic relationship between study time and exam score.
================================================================================
"""

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