"""
================================================================================
PRACTICAL 5: A/B TESTING (TWO-SAMPLE INDEPENDENT t-TEST)
================================================================================
FULL QUESTIONS:

A/B Testing Analysis:
An online platform conducts an A/B test with two versions of a landing page:
- Group A: 20 user engagement scores [42, 38, 45, 51, 47, 39, 44, 50, 46, 41, 43, 48, 37, 49, 45, 40, 52, 44, 46, 43]
- Group B: 20 user engagement scores [48, 52, 55, 49, 58, 51, 54, 56, 50, 53, 57, 49, 55, 52, 59, 54, 51, 56, 53, 55]

Hypotheses:
- H0: mu_A = mu_B (Means for both groups are same)
- H1: mu_A != mu_B (Means for both groups are not same)

Tasks:
1. Compute Mean Engagement for Group A and Group B.
2. Perform Welch's two-sample independent t-test (ttest_ind, equal_var=False).
3. Evaluate p-value at significance level alpha = 0.05.
4. Output decision: Reject H0 or Fail to Reject H0.
================================================================================
"""

import numpy as np
from scipy.stats import ttest_ind

print("H0: mu_A = mu_B")
print("H1: mu_A != mu_B\n")

group_A = np.array([
    42, 38, 45, 51, 47, 39, 44, 50, 46, 41,
    43, 48, 37, 49, 45, 40, 52, 44, 46, 43
])
group_B = np.array([
    48, 52, 55, 49, 58, 51, 54, 56, 50, 53,
    57, 49, 55, 52, 59, 54, 51, 56, 53, 55
])

mean_A = np.mean(group_A)
mean_B = np.mean(group_B)

t_stat, p_value = ttest_ind(group_A, group_B, equal_var=False)

print("Mean Engagement - Group A:", mean_A)
print("Mean Engagement - Group B:", mean_B)
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("\nReject H0: The means of both group differs significantly")
else:
    print("\nFail to Reject H0: The means of both group do not differs significantly")