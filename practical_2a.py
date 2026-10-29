"""
================================================================================
PRACTICAL 2: PROBABILITY DISTRIBUTIONS (NORMAL, BINOMIAL, POISSON)
================================================================================
FULL QUESTIONS:

Q1) Normal Distribution:
    Plot a Normal Distribution with mean (mu) = 70 and standard deviation (sigma) = 10
    over the range x in [20, 120].
    Interpret: The curve is symmetric, centered at 70, and bell-shaped.

Q2) Effect of Standard Deviation on Normal Distribution:
    Fix mean mu = 70. Plot three normal curves with standard deviations sigma = 5, 10, 15.
    Interpret: 
    - sigma = 5 is the most concentrated/tallest.
    - sigma = 15 has the greatest spread/flattest.
    - As sigma increases, the peak height decreases and spread increases.

Q3) Effect of Mean on Normal Distribution:
    Fix standard deviation sigma = 10. Plot three normal curves with means mu = 50, 70, 90.
    Interpret:
    - When mean changes with constant sigma, the normal curve shifts horizontally
      along the x-axis. Its shape, spread, and height remain unchanged.

Q4) Binomial Distribution:
    Plot the Probability Mass Function (PMF) of a Binomial Distribution for n = 20 customers
    with probability of purchase p = 0.3.
    Interpret: Represents the discrete likelihood of different numbers of customer purchases.

Q5) Poisson Distribution:
    Plot the PMF of a Poisson Distribution with an average rate lambda = 4 calls per minute
    over x = 0 to 14.
    Interpret: Poisson is a discrete distribution where expected number of calls equals lambda = 4.
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Q1) Normal Distribution
mu = 70
sigma = 10
x = np.linspace(20, 120, 500)
pdf = stats.norm.pdf(x, loc=mu, scale = sigma)
plt.plot(x,pdf)
plt.xlabel("X")
plt.ylabel("Density")
plt.title("Normal Distribution")
plt.grid()
plt.show()

# Q2) Effect of Standard Deviation
mu = 70
x = np.linspace(20, 120, 500)
pdf1 = stats.norm.pdf(x, loc=mu, scale = 5)
pdf2 = stats.norm.pdf(x, loc=mu, scale = 10)
pdf3 = stats.norm.pdf(x, loc=mu, scale = 15)
plt.figure(figsize=(9,5))
plt.plot(x, pdf1, label="sigma = 5")
plt.plot(x, pdf2, label="sigma = 10")
plt.plot(x, pdf3, label="sigma = 15")
plt.xlabel("Marks")
plt.ylabel("Probability Density Function")
plt.title("Effect of Standard Deviation and Norrmal Distribution")
plt.legend()
plt.grid(alpha = 0.3)
plt.show()

# Q3) Effect of Mean
sigma= 10
x = np.linspace(20, 120, 500)
pdf1 = stats.norm.pdf(x, loc=50, scale = sigma)
pdf2 = stats.norm.pdf(x, loc=70, scale = sigma)
pdf3 = stats.norm.pdf(x, loc=90, scale = sigma)
plt.figure(figsize=(9,5))
plt.plot(x, pdf1, label="mean = 5")
plt.plot(x, pdf2, label="mean = 10")
plt.plot(x, pdf3, label="mean = 15")
plt.xlabel("Marks")
plt.ylabel("Probability Density Function")
plt.title("Effect of Mean and Norrmal Distribution")
plt.legend()
plt.grid(alpha = 0.3)
plt.show()

# Q4) Binomial Distribution
import numpy as np
n = 20
p = 0.3
x = np.arange(0, n+1)
pmf = stats.binom.pmf(x, n ,p)
plt.stem(x, pmf)
plt.xlabel("Number of Purchases")
plt.ylabel("Probbaility")
plt.title("Binomial Distribution")
plt.grid()
plt.show()

# Q5) Poisson Distribution
lam = 4
x = np.arange(0, 15)
pmf = stats.poisson.pmf(x, mu=lam)
plt.stem(x, pmf)
plt.xlabel("Number of Calls")
plt.ylabel("Probability")
plt.title("Poisson Distribution")
plt.grid()
plt.show()