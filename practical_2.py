"""
================================================================================
PRACTICAL 2: PROBABILITY DISTRIBUTIONS (NORMAL, BINOMIAL, POISSON)
================================================================================
FULL QUESTIONS:

Q1) Normal Distribution:
    Generate values of X from 20 to 120 and calculate the probability density function
    of X ~ N(mu=70, sigma=10).
    Plot the Normal distribution curve.
    Observe the graph and state:
    1. Is the distribution symmetric?
    2. Around which value is the curve centred?
    3. What happens to the spread if standard deviation is increased?

Q2) Effect of Standard Deviation (Spread):
    Plot three Normal distributions having the same mean = 70 but different standard
    deviations 5, 10, 15.
    Use the same graph to compare their shapes:
    1. Which distribution is the most concentrated?
    2. Which distribution has the greatest spread?
    3. What happens to the height of the curve as standard deviation increases?

Q3) Effect of Mean (Horizontal Shift):
    Plot three Normal distributions having the same standard deviation = 10 but different
    means: N(50, 10^2), N(70, 10^2), N(90, 10^2).
    1. What happens to the Normal distribution when the mean changes while the standard
       deviation remains constant?

Q4) Binomial Distribution (Customer Purchases):
    Consider a situation where a customer either purchases a product or does not purchase.
    Suppose the probability of purchase is p = 0.3.
    If n = 20 customers are observed, calculate and plot the probability mass function (PMF).

Q5) Poisson Distribution (Call Center Arrivals):
    A customer-support centre receives an average of 4 calls per minute (lambda = 4).
    Model the number of calls received in one minute using a Poisson distribution and
    plot its PMF.
    1. What is the value of lambda?
    2. Is the Poisson distribution discrete or continuous?
    3. What is the expected number of calls per minute?
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ------------------------------------------------------------------------------
# Q1: Normal Distribution Curve X ~ N(70, 10^2)
# ------------------------------------------------------------------------------
mu = 70
sigma = 10
x = np.linspace(20, 120, 500)
pdf = stats.norm.pdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(8, 5))
plt.plot(x, pdf)
plt.xlabel("X")
plt.ylabel("Normal Distribution")
plt.title("Normal Distribution X ~ N(70, 10^2)")
plt.grid(True)
plt.show()

"""
Q1 Observations:
1. Yes, it is symmetric.
2. At 70 the curve is centered.
3. The curve becomes more spread.
"""

# ------------------------------------------------------------------------------
# Q2: Same Mean (70), Different Standard Deviations (5, 10, 15)
# ------------------------------------------------------------------------------
mu = 70
x = np.linspace(20, 120, 500)

pdf1 = stats.norm.pdf(x, loc=mu, scale=5)
pdf2 = stats.norm.pdf(x, loc=mu, scale=10)
pdf3 = stats.norm.pdf(x, loc=mu, scale=15)

plt.figure(figsize=(9, 5))
plt.plot(x, pdf1, label="sigma=5")
plt.plot(x, pdf2, label="sigma=10")
plt.plot(x, pdf3, label="sigma=15")

plt.xlabel("Marks")
plt.ylabel("Probability Density")
plt.title("Effect of Standard Deviation on Normal Distribution")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

"""
Q2 Observations:
1. Most concentrated: The distribution with sigma = 5.
2. Greatest spread: The distribution with sigma = 15.
3. Height of the curve: It decreases, making the curve flatter as sigma increases.
"""

# ------------------------------------------------------------------------------
# Q3: Same Standard Deviation (10), Different Means (50, 70, 90)
# ------------------------------------------------------------------------------
sigma = 10
x = np.linspace(20, 120, 500)

pdf_m50 = stats.norm.pdf(x, loc=50, scale=sigma)
pdf_m70 = stats.norm.pdf(x, loc=70, scale=sigma)
pdf_m90 = stats.norm.pdf(x, loc=90, scale=sigma)

plt.figure(figsize=(9, 5))
plt.plot(x, pdf_m50, label="mu=50")
plt.plot(x, pdf_m70, label="mu=70")
plt.plot(x, pdf_m90, label="mu=90")

plt.xlabel("Marks")
plt.ylabel("Probability Density")
plt.title("Effect of Mean on Normal Distribution")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

"""
Q3 Observation:
1. The entire distribution shifts horizontally along the x-axis without changing its shape or spread.
"""

# ------------------------------------------------------------------------------
# Q4: Binomial Distribution (n=20, p=0.3)
# ------------------------------------------------------------------------------
n = 20
p = 0.3
x = np.arange(0, n + 1)
pmf = stats.binom.pmf(x, n, p)

plt.figure(figsize=(8, 5))
plt.stem(x, pmf)
plt.xlabel("Number of Purchases")
plt.ylabel("Probability")
plt.title("Binomial Distribution (n=20, p=0.3)")
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------
# Q5: Poisson Distribution (lambda = 4 calls/minute)
# ------------------------------------------------------------------------------
lam = 4
x = np.arange(0, 20)
pmf = stats.poisson.pmf(x, lam)

plt.figure(figsize=(8, 5))
plt.stem(x, pmf)
plt.xlabel("Number of Calls")
plt.ylabel("Probability")
plt.title("Poisson Distribution (lambda=4)")
plt.grid(True)
plt.show()

"""
Q5 Observations:
1. lambda = 4.
2. Distribution is discrete.
3. The expected number of calls is 4.
"""