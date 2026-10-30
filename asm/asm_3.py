"""
================================================================================
PRACTICAL 3: ESTIMATION & CONFIDENCE INTERVALS (t-BASED & BOOTSTRAP)
================================================================================
FULL QUESTIONS:

Q1) t-based Confidence Interval:
    A sample of 20 food delivery times (in minutes) was recorded:
    [31, 28, 35, 42, 30, 27, 39, 33, 29, 45, 34, 31, 38, 26, 32, 41, 30, 36, 29, 37]
    1. Calculate sample mean and sample standard deviation (ddof=1).
    2. Determine degrees of freedom (df = n - 1).
    3. Calculate Standard Error (SE = s / sqrt(n)).
    4. Find the critical t-value for 95% confidence interval.
    5. Compute Margin of Error and 95% Confidence Interval.

Q2) Bootstrap Confidence Interval:
    Using the same delivery time data:
    1. Resample with replacement 5000 times to create bootstrap sample means.
    2. Compute the 95% percentile bootstrap confidence interval (2.5th and 97.5th percentiles).

Q3) Comparison:
    Compare the t-based CI and Bootstrap CI:
    1. Display intervals side-by-side.
    2. Compare the widths of both confidence intervals.
================================================================================
"""

import numpy as np
from scipy import stats

# ------------------------------------------------------------------------------
# Q1: t-based Confidence Interval
# ------------------------------------------------------------------------------
delivery_time = np.array([
    31, 28, 35, 42, 30,
    27, 39, 33, 29, 45,
    34, 31, 38, 26, 32,
    41, 30, 36, 29, 37
])
n = len(delivery_time)

# Sample mean and standard deviation
s_mean = np.mean(delivery_time)
s_std = np.std(delivery_time, ddof=1)

# Degrees of freedom
df = n - 1

# Standard error
SE = s_std / np.sqrt(n)

# 95% confidence interval
t_critical = stats.t.ppf(0.975, df)
margin_error = t_critical * SE

lower = s_mean - margin_error
upper = s_mean + margin_error

print("--- Q1: t-based Confidence Interval ---")
print("Sample Mean = ", s_mean)
print("Sample SD = ", s_std)
print("Degrees of freedom = ", df)
print("Standard Error = ", SE)
print("Margin of error = ", margin_error)
print("95% Confidence Interval = ", (lower, upper))

# ------------------------------------------------------------------------------
# Q2: Bootstrap Confidence Interval (5000 Resamples)
# ------------------------------------------------------------------------------
np.random.seed(42)
bootstrap_mean = []

for i in range(5000):
    bootstrap_sample = np.random.choice(delivery_time, size=n, replace=True)
    bootstrap_mean.append(np.mean(bootstrap_sample))

bootstrap_means = np.array(bootstrap_mean)

# 95% percentile bootstrap CI
lower_bootstrap = np.percentile(bootstrap_means, 2.5)
upper_bootstrap = np.percentile(bootstrap_means, 97.5)

print("\n--- Q2: Bootstrap Confidence Interval ---")
print("Bootstrap Mean = ", np.mean(bootstrap_means))
print("95% Confidence Interval = ", (lower_bootstrap, upper_bootstrap))

# ------------------------------------------------------------------------------
# Q3: Comparison
# ------------------------------------------------------------------------------
print("\n--- Q3: CI Comparison ---")
print("t-based CI =", (lower, upper))
print("bootstrap CI =", (lower_bootstrap, upper_bootstrap))

print("t-based CI width =", upper - lower)
print("bootstrap CI width =", upper_bootstrap - lower_bootstrap)