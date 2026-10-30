"""
================================================================================
PRACTICAL 6: LINEAR REGRESSION & SPEARMAN CORRELATION
================================================================================
FULL QUESTIONS:

Q1) Simple Linear Regression:
    Load the scikit-learn Diabetes dataset into a pandas DataFrame.
    1. Evaluate the Pearson linear correlation between Body Mass Index ('bmi') and disease progression ('target').
    2. Fit an Ordinary Least Squares (OLS) Simple Linear Regression model (target ~ bmi + intercept) using statsmodels.
    3. Formulate the regression equation and calculate R-squared.

Q2) Multiple Linear Regression:
    Fit an OLS Multiple Linear Regression model predicting disease progression ('target')
    using three predictors: 'bmi', blood pressure ('bp'), and 'age'.
    Evaluate:
    - R-squared and Adjusted R-squared.
    - Which individual predictors are statistically significant.
    - Write down the Multiple Linear Regression equation.

Q3) Spearman Rank Correlation:
    Given:
    study_time = [2, 4, 1, 5, 3]
    exam_score = [50, 65, 45, 80, 60]
    Calculate the Spearman rank correlation coefficient and p-value.
    Interpret the relationship.
================================================================================
"""

from sklearn.datasets import load_diabetes
import pandas as pd
import statsmodels.api as sm
from scipy.stats import spearmanr

# ------------------------------------------------------------------------------
# Q1: Simple Linear Regression
# ------------------------------------------------------------------------------
diabetes = load_diabetes(as_frame=True)
df = diabetes.frame
print("--- Diabetes Dataset Head ---")
print(df.head())

# Correlation
print("
--- Pearson Correlation: BMI vs Target ---")
print(df[["bmi", "target"]].corr())

# Simple linear regression
X = sm.add_constant(df["bmi"])
y = df["target"]
model = sm.OLS(y, X).fit()
print("
--- Simple OLS Model Summary ---")
print(model.summary())

"""
Q1 Ans:
Pearson Correlation: r = 0.5865
There is a moderate positive relationship between BMI and disease progression.
Regression Equation: Y = 152.1335 + 949.4353 * (BMI)
R^2 = 0.3439
Therefore, BMI explains 34.39% of the variation in disease progression.
"""

# ------------------------------------------------------------------------------
# Q2: Multiple Linear Regression
# ------------------------------------------------------------------------------
X_multi = df[["bmi", "bp", "age"]]
X_multi = sm.add_constant(X_multi)
model_multi = sm.OLS(df["target"], X_multi).fit()
print("
--- Multiple OLS Model Summary ---")
print(model_multi.summary())

"""
Q2 Ans:
R^2 = 0.396, Adjusted R^2 = 0.392
Significant Predictors:
- BMI -> Significant (p < 0.001)
- BP  -> Significant (p < 0.001)
- Age -> Not Significant (p = 0.685)
Regression Equation:
Y = 152.1335 + 788.7827(BMI) + 394.1271(BP) + 25.9904(Age)
Conclusion:
BMI and BP are significant predictors of disease progression, while Age is not significant.
"""

# ------------------------------------------------------------------------------
# Q3: Spearman Rank Correlation
# ------------------------------------------------------------------------------
study_time = [2, 4, 1, 5, 3]
exam_score = [50, 65, 45, 80, 60]
correlation, p_value = spearmanr(study_time, exam_score)

print("
--- Spearman Rank Correlation ---")
print("Spearman's correlation coefficient:", correlation)
print("p-value:", p_value)

"""
Q3 Ans:
Study Time & Exam score are perfectly positively correlated (rho = 1.0, p = 1.40e-24).
"""
