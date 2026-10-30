"""
================================================================================
PRACTICAL 4: HYPOTHESIS TESTING (t-TEST, CHI-SQUARE, ANOVA & TUKEY HSD)
================================================================================
FULL QUESTIONS:

Q1) Two-Sample Independent t-Test (Welch's t-test):
    Test whether the mean fare paid by male and female Titanic passengers differs significantly.
    - H0: The mean fare paid by male and female passengers differs insignificantly.
    - H1: The mean fare paid by male and female passengers differs significantly.

Q2a) Chi-Square Test of Independence:
    Test whether passenger class ('class') and survival status ('survived') are associated.
    - H0: The passenger class and the survival status are not associated.
    - H1: The passenger class and the survival status are associated.

Q2b) One-Way ANOVA & Tukey HSD Post-Hoc Test:
    Test whether mean fares differ significantly across 3 passenger classes (First, Second, Third).
    - H0: Mean fares do not differ significantly across 3 passenger classes.
    - H1: Mean fares differ significantly across 3 passenger classes.
    - Perform pairwise Tukey HSD post-hoc test to identify pairwise differences.
================================================================================
"""

import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load Titanic dataset
df = sns.load_dataset("titanic")

# ------------------------------------------------------------------------------
# Q1: Two-Sample Independent t-Test (Male vs Female Fare)
# ------------------------------------------------------------------------------
print("--- Q1: Independent Two-Sample t-Test ---")
print("H0 = the mean fare paid by male and female passenger differs insignificantly")
print("H1 = the mean fare paid by male and female passenger differs significantly\n")

male = df[df["sex"] == "male"]["fare"].dropna()
female = df[df["sex"] == "female"]["fare"].dropna()

t_stat, p_value = stats.ttest_ind(male, female, equal_var=False)
print("t-statistic :", t_stat)
print("p_value :", p_value)

if p_value < 0.05:
    print("Decision: p_value < 0.05, hence reject H0. Mean fare paid by male and female differs significantly.")
else:
    print("Decision: Fail to reject H0.")

# ------------------------------------------------------------------------------
# Q2a: Chi-Square Test of Independence (Class vs Survival)
# ------------------------------------------------------------------------------
print("\n--- Q2a: Chi-Square Test of Independence ---")
print("H0: The passenger class and the survival status are not associated")
print("H1: The passenger class and the survival status are associated\n")

table = pd.crosstab(df["class"], df["survived"])
print("Contingency Table:")
print(table)

chi2, p_value_chi, dof, expected = chi2_contingency(table)
print("\nChi square statistic :", chi2)
print("Degrees of freedom :", dof)
print("p-value :", p_value_chi)

if p_value_chi < 0.05:
    print("Decision: p-value < 0.05, hence reject H0. Passenger class and survival status are associated.")
else:
    print("Decision: Fail to reject H0.")

# ------------------------------------------------------------------------------
# Q2b: One-Way ANOVA & Tukey HSD (Fare Across Classes)
# ------------------------------------------------------------------------------
print("\n--- Q2b: One-Way ANOVA & Tukey HSD ---")
print("H0: Mean fares do not differ significantly across 3 passenger classes")
print("H1: Mean fares differ significantly across 3 passenger classes\n")

first = df[df["class"] == "First"]["fare"].dropna()
second = df[df["class"] == "Second"]["fare"].dropna()
third = df[df["class"] == "Third"]["fare"].dropna()

F, p_value_f = f_oneway(first, second, third)
print("F-statistic: ", F)
print("p_value: ", p_value_f)

df_clean = df.dropna(subset=["fare"])
tukey_result = pairwise_tukeyhsd(endog=df_clean["fare"], groups=df_clean["class"])
print("\nTukey HSD Post-Hoc Test:")
print(tukey_result)

"""
Observations:
1. First and Second group differs significantly.
2. First and Third group differs significantly.
3. Second and Third does not differ significantly.
"""