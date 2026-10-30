"""
================================================================================
PRACTICAL 4: HYPOTHESIS TESTING (T-TEST, CHI-SQUARE, ONE-WAY ANOVA & TUKEY HSD)
================================================================================
FULL QUESTIONS:

Question 1: (Two-Sample Independent t-Test)
    Using the Titanic dataset, perform Welch's independent two-sample t-test
    (equal_var=False) to test whether ticket fares paid by male vs female passengers differ.
    H0: The mean fare paid by male and female passengers differs insignificantly.
    H1: The mean fare paid by male and female passengers differs significantly.

Question 2: (Chi-Square Test of Independence)
    Using the Titanic dataset, construct a contingency table crossing passenger
    'class' (First, Second, Third) with 'survived' status (0, 1).
    Perform a Chi-Square test of independence to assess whether passenger class
    is significantly associated with survival outcome.
    H0: Passenger class and survival status are not associated.
    H1: Passenger class and survival status are associated.

Question 3: (One-Way ANOVA & Post-Hoc Tukey HSD Test)
    H0: Mean fares do not differ significantly across the three passenger classes.
    1. Perform One-Way ANOVA (f_oneway).
    2. Conduct Tukey's Honestly Significant Difference (HSD) test to identify
       which specific pairs of passenger classes differ in mean fare.
================================================================================
"""

import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ------------------------------------------------------------------------------
# Q1: Two-Sample Independent t-test
# ------------------------------------------------------------------------------
print("H0: The mean fare paid by male and female passengers differs insignificantly.")
print("H1: The mean fare paid by male and female passengers differs significantly.")

df = sns.load_dataset("titanic")

male = df[df["sex"] == "male"]["fare"].dropna()
female = df[df["sex"] == "female"]["fare"].dropna()

t_stat, p_value = stats.ttest_ind(
    male, female, equal_var=False
)

print("
t-statistic:", t_stat)
print("p_value:", p_value)

# ------------------------------------------------------------------------------
# Q2: Chi-Square Test of Independence
# ------------------------------------------------------------------------------
print("
" + "="*50)
print("H0: Passenger class and survival status are not associated.")
print("H1: Passenger class and survival status are associated.")

table = pd.crosstab(df["class"], df["survived"])
print("
Contingency Table:")
print(table)

chi2, p_value, dof, expected = chi2_contingency(table)

print("
chi-square statistic:", chi2)
print("Degrees of freedom:", dof)
print("p_value:", p_value)

# ------------------------------------------------------------------------------
# Q3: One-Way ANOVA & Post-Hoc Tukey HSD
# ------------------------------------------------------------------------------
print("
" + "="*50)
print("One-Way ANOVA across Passenger Classes:")

first = df[df["class"] == "First"]["fare"].dropna()
second = df[df["class"] == "Second"]["fare"].dropna()
third = df[df["class"] == "Third"]["fare"].dropna()

F, p_value = f_oneway(first, second, third)

print("F-statistic:", F)
print("p_value:", p_value)

print("
Tukey HSD Post-Hoc Test:")
df_clean = df.dropna(subset=["fare"])
tukey = pairwise_tukeyhsd(endog=df_clean["fare"], groups=df_clean["class"])
print(tukey)

"""
Interpretation:
First and Second & First and Third mean fares differ significantly (reject=True).
Second and Third fares do not differ significantly (reject=False, p-adj = 0.108).
"""
