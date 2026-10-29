"""
================================================================================
PRACTICAL 3: CONFIDENCE INTERVALS & BOOTSTRAPPING
================================================================================
FULL QUESTIONS:

Question 1: (Parametric Student's t-based Confidence Interval)
    Given delivery times (in minutes) for 20 orders:
    [31, 28, 35, 42, 30, 27, 39, 33, 26, 32, 34, 31, 38, 26, 32, 41, 30, 36, 29, 37]
    1. Calculate the sample mean and sample standard deviation (ddof=1).
    2. Determine degrees of freedom (df = n - 1) and standard error (SE = s / sqrt(n)).
    3. Compute the 95% Confidence Interval for the population mean delivery time
       using the Student's t-distribution critical value.

Question 2: (Non-Parametric Bootstrap Confidence Interval)
    1. Estimate the 95% Confidence Interval for the mean delivery time using Bootstrapping
       with 5,000 resamples (sampling with replacement, random seed 42).
    2. Calculate the 2.5th and 97.5th percentiles of the bootstrap distribution.
    3. Compare the t-based CI and Bootstrap CI in terms of range and interval width.
================================================================================
"""

from scipy import stats
import numpy as np

delivery_time = np.array([
    31, 28, 35, 42, 30,
    27, 39, 33, 26, 32,
    34, 31, 38, 26, 32,
    41, 30, 36, 29, 37
])

n = len(delivery_time)

# Sample mean and sample standard deviation
sample_mean = np.mean(delivery_time)
sample_sd = np.std(delivery_time, ddof = 1) # for population ddof=0

# Degrees of Freedom
df = n - 1

# Standard Error
SE = sample_sd / np.sqrt(n)

# 95% confidence interval
t_critical = stats.t.ppf(0.975, df)
margin_error = t_critical * SE
lower = sample_mean - margin_error
upper = sample_mean + margin_error

print("Sample Mean =", sample_mean)
print("Sample SD =", sample_sd)
print("Degrees of Freedom =", df)
print("Standard Error =", SE)
print("Margin of Error =", margin_error)
print("95% Confidence Interval =", (lower, upper))

# Question 2: Bootstrap Confidence Interval
np.random.seed(42)
bootstrap_means = []

for i in range(5000):
  bootstrap_sample = np.random.choice(
      delivery_time,
      size=len(delivery_time),
      replace=True
  )
  bootstrap_means.append(np.mean(bootstrap_sample))

bootstrap_means = np.array(bootstrap_means)

# 95% percentile bootstrap CI
lower_bootstrap = np.percentile(bootstrap_means, 2.5)
upper_bootstrap = np.percentile(bootstrap_means, 97.5)

print("Bootstrap Mean =", np.mean(bootstrap_means))
print("95% Bootstrap CI =", (lower_bootstrap, upper_bootstrap))

print("t-based CI =", (lower, upper))
print("Bootstrap CI =", (lower_bootstrap, upper_bootstrap))
print("t-based CI width =", lower - upper)
print("Bootstrap CI width =", upper_bootstrap - lower_bootstrap)