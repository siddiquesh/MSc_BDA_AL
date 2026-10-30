"""
================================================================================
PRACTICAL 3: CONFIDENCE INTERVALS & BOOTSTRAPPING
================================================================================
FULL QUESTIONS:

Question 1: (Parametric Student's t-based 95% Confidence Interval)
    Given delivery times (in minutes) for 20 orders:
    [31, 28, 35, 42, 30, 27, 39, 33, 29, 45, 34, 31, 38, 26, 32, 41, 30, 36, 29, 37]
    1. Calculate the sample mean and sample standard deviation (ddof=1).
    2. Determine degrees of freedom (df = n - 1) and standard error (SE = s / sqrt(n)).
    3. Compute the 95% Confidence Interval for the mean delivery time using Student's t-distribution.

Question 2: (Non-Parametric Bootstrap Confidence Interval)
    1. Estimate the 95% Confidence Interval for the mean delivery time using Bootstrapping
       with 5,000 resamples (sampling with replacement, random seed 42).
    2. Calculate the 2.5th and 97.5th percentiles of the bootstrap distribution.
    3. Compare the t-based CI and Bootstrap CI in terms of range and interval width.
================================================================================
"""

import numpy as np
from scipy import stats

# ------------------------------------------------------------------------------
# Q1: Parametric Student's t-based CI
# ------------------------------------------------------------------------------
delivery_time = np.array([
    31, 28, 35, 42, 30,
    27, 39, 33, 29, 45,
    34, 31, 38, 26, 32,
    41, 30, 36, 29, 37
])
n = len(delivery_time)

# Sample Mean & Standard Deviation
sample_mean = np.mean(delivery_time)
sample_sd = np.std(delivery_time, ddof=1)

# Degrees of freedom
df = n - 1

# Standard Error
SE = sample_sd / np.sqrt(n)

# 95% confidence interval
t_critical = stats.t.ppf(0.975, df)
margin_error = t_critical * SE

lower = sample_mean - margin_error
upper = sample_mean + margin_error

print("sample mean =", sample_mean)
print("Sample Sd =", sample_sd)
print("Degrees of freedom =", df)
print("Standard Error =", SE)
print("margin of error =", margin_error)
print("95% confidence interval =", (lower, upper))

# ------------------------------------------------------------------------------
# Q2: Non-Parametric Bootstrap CI (5,000 Resamples)
# ------------------------------------------------------------------------------
np.random.seed(42)
bootstrap_mean = []

for i in range(5000):
    bootstrap_sample = np.random.choice(
        delivery_time,
        size=len(delivery_time),
        replace=True
    )
    bootstrap_mean.append(np.mean(bootstrap_sample))

bootstrap_mean = np.array(bootstrap_mean)

# 95% percentile bootstrap CI
lower_bootstrap = np.percentile(bootstrap_mean, 2.5)
upper_bootstrap = np.percentile(bootstrap_mean, 97.5)

print("
Bootstrap Mean =", np.mean(bootstrap_mean))
print("95% Bootstrap CI =", (lower_bootstrap, upper_bootstrap))

# ------------------------------------------------------------------------------
# Comparison
# ------------------------------------------------------------------------------
print("
t-based CI =", (lower, upper))
print("bootstrap CI =", (lower_bootstrap, upper_bootstrap))
print("t-based CI width =", upper - lower)
print("bootstrap CI width =", upper_bootstrap - lower_bootstrap)
