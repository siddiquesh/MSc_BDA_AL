"""
================================================================================
PRACTICAL 5: A/B TESTING ANALYSIS
================================================================================
FULL QUESTIONS:

Question: (A/B Testing Analysis with Two-Sample Welch's t-Test)
    Given conversion / performance metrics from an A/B test with 20 users per group:
    - Control Group A:
      [42, 38, 45, 51, 47, 39, 44, 50, 46, 41, 43, 48, 37, 49, 45, 40, 52, 44, 46, 43]
    - Treatment Variant Group B:
      [48, 52, 55, 49, 58, 51, 54, 56, 50, 53, 57, 49, 55, 52, 59, 54, 51, 56, 53, 55]

    H0: Means for both groups are the same.
    H1: Means for both groups are not the same.

    1. Calculate the sample mean for Group A and Group B.
    2. Conduct an independent two-sample t-test (Welch's t-test, equal_var=False).
    3. Automate decision rule: Reject H0 if p-value < 0.05.
================================================================================
"""

import numpy as np
from scipy.stats import ttest_ind

print("H0: Means for both groups are same.")
print("H1: Means for both groups are not same.
")

group_A = np.array([
    42, 38, 45, 51, 47, 39, 44, 50, 46, 41, 43, 48, 37, 49, 45, 40, 52, 44, 46, 43
])
group_B = np.array([
    48, 52, 55, 49, 58, 51, 54, 56, 50, 53, 57, 49, 55, 52, 59, 54, 51, 56, 53, 55
])

mean_A = np.mean(group_A)
mean_B = np.mean(group_B)

t_stat, p_value = ttest_ind(group_A, group_B, equal_var=False)

print("Mean - Group A:", mean_A)
print("Mean - Group B:", mean_B)
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("
Decision: Reject H0 -> The means of both groups differ significantly.")
else:
    print("
Decision: Fail to reject H0 -> The means of both groups do not differ significantly.")
