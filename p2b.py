"""
================================================================================
PRACTICAL 2: PROBABILITY DISTRIBUTIONS (NORMAL, BINOMIAL, POISSON)
================================================================================
FULL QUESTIONS:

Q1) Generate values of X from 20 to 120 and calculate the probability density function
    of X ~ N(70, 10^2). Plot the Normal distribution curve.
    Observe the graph and state:
    1. Is the distribution symmetric?
    2. Around which value is the curve centered?
    3. What happens to the spread if standard deviation is increased?

Q2) Plot three Normal distributions having the same mean = 70 but different standard
    deviations: 5, 10, 15. Use the same graph to compare their shapes.
    Observe the graph and answer:
    i) Which distribution is the most concentrated?
    ii) Which distribution has the greatest spread?
    iii) What happens to the height of the curve as standard deviation increases?

Q3) Plot three Normal distributions having the same standard deviation (sigma = 10)
    but different means: N(50, 10^2), N(70, 10^2), N(90, 10^2).
    What happens to the Normal distribution when the mean changes while the
    standard deviation remains constant?

Q4) Consider a situation where a customer either purchases a product or does not purchase.
    Suppose the probability of purchase is p = 0.3. If 20 customers are observed,
    calculate and plot the probability mass function (Binomial Distribution).

Q5) A customer-support center receives an average of 4 calls per minute.
    Model the number of calls received in one minute using a Poisson distribution
    and plot its probability mass function.
    Answer:
    1. What is the value of lambda?
    2. Is the Poisson distribution discrete or continuous?
    3. What is the expected number of calls per minute?
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ------------------------------------------------------------------------------
# Q1: Normal Distribution
# ------------------------------------------------------------------------------
mu = 70
sigma = 10
x = np.linspace(20, 120, 500)
pdf = stats.norm.pdf(x, loc=mu, scale=sigma)

plt.plot(x, pdf)
plt.xlabel("X")
plt.ylabel("Density")
plt.title("Normal Distribution")
plt.grid()
plt.show()

"""
Q1 Answers:
1. Yes, it is symmetric.
2. The curve is centered at 70.
3. If standard deviation is increased, the curve becomes more spread out and flatter.
"""

# ------------------------------------------------------------------------------
# Q2: Effect of Standard Deviation on Normal Distribution
# ------------------------------------------------------------------------------
mu = 70
x = np.linspace(20, 120, 200)

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
Q2 Answers:
i) The distribution with sigma = 5 is the most concentrated (tallest peak).
ii) The distribution with sigma = 15 has the greatest spread (widest tails).
iii) As standard deviation increases, the peak height of the curve decreases.
"""

# ------------------------------------------------------------------------------
# Q3: Effect of Mean on Normal Distribution
# ------------------------------------------------------------------------------
sigma = 10
x = np.linspace(20, 120, 200)

pdf1 = stats.norm.pdf(x, loc=50, scale=sigma)
pdf2 = stats.norm.pdf(x, loc=70, scale=sigma)
pdf3 = stats.norm.pdf(x, loc=90, scale=sigma)

plt.figure(figsize=(9, 5))
plt.plot(x, pdf1, label="mean=50")
plt.plot(x, pdf2, label="mean=70")
plt.plot(x, pdf3, label="mean=90")
plt.xlabel("Marks")
plt.ylabel("Probability Density")
plt.title("Effect of Mean on Normal Distribution")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

"""
Q3 Answer:
When the mean changes while standard deviation remains constant, there is a horizontal
shift of the curve along the x-axis with no change in scale, spread, or height.
"""

# ------------------------------------------------------------------------------
# Q4: Binomial Distribution
# ------------------------------------------------------------------------------
n = 20
p = 0.3

x = np.arange(0, n + 1)
pmf = stats.binom.pmf(x, n, p)

plt.stem(x, pmf)
plt.xlabel("Number of Purchases")
plt.ylabel("Probability")
plt.title("Binomial Distribution (n=20, p=0.3)")
plt.grid()
plt.show()

"""
Q4 Answer:
Shows the PMF for 20 customers with purchase probability 0.3. Highest probability peaks around n*p = 6.
"""

# ------------------------------------------------------------------------------
# Q5: Poisson Distribution
# ------------------------------------------------------------------------------
lam = 4

x = np.arange(0, 15)
pmf = stats.poisson.pmf(x, mu=lam)

plt.stem(x, pmf)
plt.xlabel("Number of Calls")
plt.ylabel("Probability")
plt.title("Poisson Distribution (lambda=4)")
plt.grid()
plt.show()

"""
Q5 Answers:
1. Value of lambda is 4.
2. The Poisson distribution is discrete.
3. The expected number of calls per minute is equal to lambda = 4.
"""
