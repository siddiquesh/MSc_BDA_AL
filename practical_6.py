"""
================================================================================
PRACTICAL 6: REGRESSION ANALYSIS (SIMPLE, MULTIPLE & SPEARMAN RANK)
================================================================================
FULL QUESTIONS:

Q1) Simple Linear Regression:
    1. Load the Diabetes Dataset from sklearn.datasets.
    2. Compute Pearson correlation between BMI and disease progression (target).
    3. Fit a Simple Linear Regression model: target = beta0 + beta1 * BMI.
    4. Display OLS regression summary and provide slope interpretation.

Q2) Multiple Linear Regression:
    1. Fit Multiple Linear Regression with predictors: BMI, BP (blood pressure), Age.
    2. Display OLS regression summary.
    3. Provide interpretation of significant predictors (p < 0.05) and insignificant predictors.

Q3) Spearman Rank Correlation:
    Given two variables:
    Study Time: [2, 4, 1, 5, 3]
    Exam Score: [50, 65, 45, 80, 60]
    1. Compute Spearman's rank correlation coefficient and p-value.
    2. State the monotonic relationship.
================================================================================
"""

from sklearn.datasets import load_diabetes
import pandas as pd
import statsmodels.api as sm
from scipy.stats import spearmanr

# ------------------------------------------------------------------------------
# Q1: Simple Linear Regression (BMI vs Target)
# ------------------------------------------------------------------------------
diabetes = load_diabetes(as_frame=True)
df = diabetes.frame
print("--- Diabetes Dataset Head ---")
print(df.head())

# Correlation
print("\n--- Correlation ---")
print(df[['bmi', 'target']].corr())

# Simple linear regression
x = sm.add_constant(df['bmi'])
y = df['target']
model = sm.OLS(y, x).fit()
print("\n--- Regression Summary ---")
print(model.summary())

"""
Slope interpretation:
For every one-unit increase in BMI, predicted Y increases by 949.4353 units on average.
"""

# ------------------------------------------------------------------------------
# Q2: Multiple Linear Regression (BMI, BP, Age vs Target)
# ------------------------------------------------------------------------------
print("\n--- Q2: Multiple Linear Regression ---")
x_multi = df[["bmi", "bp", "age"]]
x_multi = sm.add_constant(x_multi)
y = df["target"]
model_multi = sm.OLS(y, x_multi).fit()
print(model_multi.summary())

"""
Regression Coefficients Summary:
* Significant Predictors (p < 0.05):
  - BMI (coef = 788.78): Strongest positive effect. A 1-unit increase yields a ~788.8 unit increase in target.
  - BP (coef = 394.13): Positive effect. A 1-unit increase yields a ~394.1 unit increase in target.
  - Intercept (const) (coef = 152.13): Expected value of target when all predictors are zero.

* Insignificant Predictors (p >= 0.05):
  - Age (coef = 25.99, p = 0.685): No statistically significant relationship with the target in this model.
"""

# ------------------------------------------------------------------------------
# Q3: Spearman Rank Correlation (Study Time vs Exam Score)
# ------------------------------------------------------------------------------
print("\n--- Q3: Spearman Rank Correlation ---")
study_time = [2, 4, 1, 5, 3]
exam_score = [50, 65, 45, 80, 60]

correlation, p_value = spearmanr(study_time, exam_score)

print("Spearman's correlation coefficient:", correlation)
print("p-value:", p_value)

"""
Interpretation:
Spearman correlation coefficient is 1.0 -> Perfectly Positively Correlated.
"""