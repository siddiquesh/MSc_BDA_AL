# ASM Practical 5 - A/B Testing

# Dataset for A/B Testing
import numpy as np
from scipy.stats import ttest_ind

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

print("Mean - Group A:", mean_A)
print("Mean - Group B:", mean_B)
print("t-statistic:", t_stat)
print("p-value:", p_value)
