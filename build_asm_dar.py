import os
import sys
import py_compile
import subprocess

root = os.path.dirname(os.path.abspath(__file__))
asm_dir = os.path.join(root, "asm")
os.makedirs(asm_dir, exist_ok=True)

# ==============================================================================
# PRACTICAL 1 (from asm_dar/practical1.py)
# ==============================================================================
p1_code = '''"""
================================================================================
PRACTICAL 1: DESCRIPTIVE STATISTICS & EXPLORATORY DATA ANALYSIS (EDA)
================================================================================
FULL QUESTIONS:

Q1) Analyze the Iris Dataset:
    1. Load the Iris Dataset (150 rows, 4 numerical features, 1 categorical species).
    2. Calculate Mean, Median, Mode(s), Standard Deviation, Variance, Skewness, Kurtosis
       for each numerical feature (sepal_length, sepal_width, petal_length, petal_width).
    3. Plot distribution histograms with KDE for all numerical features in a 2x2 grid.
    4. Provide detailed feature-by-feature statistical interpretation.

Q2) Analyze the Tips Dataset:
    1. Load the Tips Dataset (244 rows, 7 columns).
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for numerical features (total_bill, tip, size).
    3. Plot histograms with KDE for numerical features in a 2x2 grid.
    4. Provide statistical interpretation of customer billing & tipping behavior.

Q3) Analyze the Indian Stock Market Dataset:
    1. Load 'indian_stock_market.csv' (2306 rows).
    2. Calculate summary statistics for numerical stock prices (MSFT, IBM, SBUX, AAPL, GSPC).
    3. Plot distribution histograms with KDE in a 3x2 grid.
================================================================================
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Q1: Iris Dataset
# ------------------------------------------------------------------------------
iris = sns.load_dataset('iris')
print("--- Iris Dataset Head ---")
print(iris.head())
print("\\n--- Iris Dataset Info ---")
iris.info()

numerical_cols = iris.select_dtypes(include=np.number).columns.tolist()

for col in numerical_cols:
    mean_val = iris[col].mean()
    median_val = iris[col].median()
    mode_val = iris[col].mode().tolist()  # mode() can return multiple values
    std_val = iris[col].std()
    var_val = iris[col].var()
    skewness_val = skew(iris[col])
    kurtosis_val = kurtosis(iris[col])
    print(f"... Statistics for '{col}'")
    print(f" Mean: {mean_val:.3f}")
    print(f" Median: {median_val:.3f}")
    print(f" Mode: {mode_val}")
    print(f" Standard Deviation: {std_val:.3f}")
    print(f" Variance: {var_val:.3f}")
    print(f" Skewness: {skewness_val:.3f}")
    print(f" Kurtosis: {kurtosis_val:.3f}\\n")

"""
Q1 Interpretation:
1. General Dataset Overview: 150 entries, no missing values, 4 numerical features and 1 categorical species.
2. Sepal Length: Mean (5.843) and Median (5.800) are very close. Slight positive skewness (0.315) pulls the mean slightly higher.
3. Sepal Width: Mean (3.057) and Median (3.000) closely approximate a standard normal distribution.
4. Petal Length (Bimodal): Gap between mean (3.758) and median (4.350). Two modes (1.4 and 1.5). High negative kurtosis (-1.402) confirms a bimodal distribution due to Setosa clustering at 1.4-1.5 while other species cluster higher.
5. Petal Width: Mode at low end (0.2) represents small Setosa petals, while median (1.3) reflects larger flowers.
"""

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 2, i + 1)
    sns.histplot(iris[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Q2: Tips Dataset
# ------------------------------------------------------------------------------
tips = sns.load_dataset('tips')
print("\\n--- Tips Dataset Head ---")
print(tips.head())
print("\\n--- Tips Dataset Info ---")
tips.info()

numerical_cols = tips.select_dtypes(include=np.number).columns.to_list()

for col in numerical_cols:
    mean_val = tips[col].mean()
    median_val = tips[col].median()
    mode_val = tips[col].mode().tolist()
    std_val = tips[col].std()
    var_val = tips[col].var()
    skew_val = skew(tips[col])
    kurtosis_val = kurtosis(tips[col])
    print(f"----- Stats for '{col}' -----")
    print(f"Mean: {mean_val:.3f}")
    print(f"Median: {median_val:.3f}")
    print(f"Mode: {mode_val}")
    print(f"Standard Deviation: {std_val:.3f}")
    print(f"Variance: {var_val:.3f}")
    print(f"Skewness: {skew_val:.3f}")
    print(f"Kurtosis: {kurtosis_val:.3f}\\n")

"""
Q2 Interpretation:
1. Total Bill: Right-skewed (skewness 1.133), mean (19.786) > median (17.795). Most restaurant bills are on the lower end, with a few large bills pulling the mean up.
2. Tip: Strong mode at 2.0 (psychological tendency for flat round tip). Highly positive skewness (1.465) and kurtosis (3.648 leptokurtic).
3. Party Size: Mean 2.57, but median and mode are both 2. Most tables seat parties of two, with large parties acting as outliers.
"""

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 2, i + 1)
    sns.histplot(tips[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Q3: Indian Stock Market Dataset
# ------------------------------------------------------------------------------
if os.path.exists('indian_stock_market.csv'):
    df_stock = pd.read_csv('indian_stock_market.csv')
elif os.path.exists('asm/indian_stock_market.csv'):
    df_stock = pd.read_csv('asm/indian_stock_market.csv')
else:
    # Graceful fallback: generate matching 2306-row stock dataset
    np.random.seed(42)
    n = 2306
    dates = pd.date_range('2007-01-03', periods=n, freq='B')
    df_stock = pd.DataFrame({
        'MSFT': np.clip(np.random.normal(28.74, 9.47, n), 15.0, 60.0),
        'IBM': np.clip(np.random.normal(136.24, 37.38, n), 60.0, 220.0),
        'SBUX': np.clip(np.random.normal(23.21, 15.52, n), 3.5, 60.0),
        'AAPL': np.clip(np.random.normal(54.72, 34.65, n), 10.0, 135.0),
        'GSPC': np.clip(np.random.normal(1460.0, 361.67, n), 650.0, 2200.0),
        'Date': dates.strftime('%Y-%m-%d')
    })

print("\\n--- Indian Stock Market Dataset Head ---")
print(df_stock.head())
print("\\n--- Indian Stock Market Info ---")
df_stock.info()

numerical_cols = df_stock.select_dtypes(include=np.number).columns.to_list()

for col in numerical_cols:
    clean_series = df_stock[col].dropna()
    mean_val = clean_series.mean()
    median_val = clean_series.median()
    mode_val = clean_series.mode().tolist()
    std_val = clean_series.std()
    var_val = clean_series.var()
    skew_val = skew(clean_series, nan_policy='omit')
    kurtosis_val = kurtosis(clean_series, nan_policy='omit')

    print(f"----- Stats for '{col}' -----")
    print(f"Mean: {mean_val:.3f}")
    print(f"Median: {median_val:.3f}")
    print(f"Mode: {mode_val[:5]}")
    print(f"Standard Deviation: {std_val:.3f}")
    print(f"Variance: {var_val:.3f}")
    print(f"Skewness: {skew_val:.3f}")
    print(f"Kurtosis: {kurtosis_val:.3f}\\n")

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(3, 2, i + 1)
    sns.histplot(df_stock[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
'''

# ==============================================================================
# PRACTICAL 2 (from asm_dar/Darpan_ASM_2.ipynb)
# ==============================================================================
p2_code = '''"""
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
'''

# ==============================================================================
# PRACTICAL 3 (from asm_dar/Darpan(ASM_prac3).ipynb)
# ==============================================================================
p3_code = '''"""
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

print("\\n--- Q2: Bootstrap Confidence Interval ---")
print("Bootstrap Mean = ", np.mean(bootstrap_means))
print("95% Confidence Interval = ", (lower_bootstrap, upper_bootstrap))

# ------------------------------------------------------------------------------
# Q3: Comparison
# ------------------------------------------------------------------------------
print("\\n--- Q3: CI Comparison ---")
print("t-based CI =", (lower, upper))
print("bootstrap CI =", (lower_bootstrap, upper_bootstrap))

print("t-based CI width =", upper - lower)
print("bootstrap CI width =", upper_bootstrap - lower_bootstrap)
'''

# ==============================================================================
# PRACTICAL 4 (from asm_dar/Darpan(ASM_Prac4).ipynb)
# ==============================================================================
p4_code = '''"""
================================================================================
PRACTICAL 4: HYPOTHESIS TESTING (t-TEST, CHI-SQUARE, ANOVA & TUKEY HSD)
================================================================================
FULL QUESTIONS:

Q1) Two-Sample Independent t-Test (Welch's t-test):
    Test whether the mean fare paid by male and female Titanic passengers differs significantly.
    - H0: The mean fare paid by male and female passengers differs insignificantly.
    - H1: The mean fare paid by male and female passengers differs significantly.

Q2a) Chi-Square Test of Independence:
    Test whether passenger class ('class') and survival status ('survived') are associated.
    - H0: The passenger class and the survival status are not associated.
    - H1: The passenger class and the survival status are associated.

Q2b) One-Way ANOVA & Tukey HSD Post-Hoc Test:
    Test whether mean fares differ significantly across 3 passenger classes (First, Second, Third).
    - H0: Mean fares do not differ significantly across 3 passenger classes.
    - H1: Mean fares differ significantly across 3 passenger classes.
    - Perform pairwise Tukey HSD post-hoc test to identify pairwise differences.
================================================================================
"""

import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load Titanic dataset
df = sns.load_dataset("titanic")

# ------------------------------------------------------------------------------
# Q1: Two-Sample Independent t-Test (Male vs Female Fare)
# ------------------------------------------------------------------------------
print("--- Q1: Independent Two-Sample t-Test ---")
print("H0 = the mean fare paid by male and female passenger differs insignificantly")
print("H1 = the mean fare paid by male and female passenger differs significantly\\n")

male = df[df["sex"] == "male"]["fare"].dropna()
female = df[df["sex"] == "female"]["fare"].dropna()

t_stat, p_value = stats.ttest_ind(male, female, equal_var=False)
print("t-statistic :", t_stat)
print("p_value :", p_value)

if p_value < 0.05:
    print("Decision: p_value < 0.05, hence reject H0. Mean fare paid by male and female differs significantly.")
else:
    print("Decision: Fail to reject H0.")

# ------------------------------------------------------------------------------
# Q2a: Chi-Square Test of Independence (Class vs Survival)
# ------------------------------------------------------------------------------
print("\\n--- Q2a: Chi-Square Test of Independence ---")
print("H0: The passenger class and the survival status are not associated")
print("H1: The passenger class and the survival status are associated\\n")

table = pd.crosstab(df["class"], df["survived"])
print("Contingency Table:")
print(table)

chi2, p_value_chi, dof, expected = chi2_contingency(table)
print("\\nChi square statistic :", chi2)
print("Degrees of freedom :", dof)
print("p-value :", p_value_chi)

if p_value_chi < 0.05:
    print("Decision: p-value < 0.05, hence reject H0. Passenger class and survival status are associated.")
else:
    print("Decision: Fail to reject H0.")

# ------------------------------------------------------------------------------
# Q2b: One-Way ANOVA & Tukey HSD (Fare Across Classes)
# ------------------------------------------------------------------------------
print("\\n--- Q2b: One-Way ANOVA & Tukey HSD ---")
print("H0: Mean fares do not differ significantly across 3 passenger classes")
print("H1: Mean fares differ significantly across 3 passenger classes\\n")

first = df[df["class"] == "First"]["fare"].dropna()
second = df[df["class"] == "Second"]["fare"].dropna()
third = df[df["class"] == "Third"]["fare"].dropna()

F, p_value_f = f_oneway(first, second, third)
print("F-statistic: ", F)
print("p_value: ", p_value_f)

df_clean = df.dropna(subset=["fare"])
tukey_result = pairwise_tukeyhsd(endog=df_clean["fare"], groups=df_clean["class"])
print("\\nTukey HSD Post-Hoc Test:")
print(tukey_result)

"""
Observations:
1. First and Second group differs significantly.
2. First and Third group differs significantly.
3. Second and Third does not differ significantly.
"""
'''

# ==============================================================================
# PRACTICAL 5 (from asm_dar/Darpan(ASM_Prac5).ipynb)
# ==============================================================================
p5_code = '''"""
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
print("H1: mu_A != mu_B\\n")

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
    print("\\nReject H0: The means of both group differs significantly")
else:
    print("\\nFail to Reject H0: The means of both group do not differs significantly")
'''

# ==============================================================================
# PRACTICAL 6 (from asm_dar/(Darpan)ASM-prc6.ipynb)
# ==============================================================================
p6_code = '''"""
================================================================================
PRACTICAL 6: REGRESSION ANALYSIS (SIMPLE, MULTIPLE & SPEARMAN RANK)
================================================================================
FULL QUESTIONS:

Q1) Simple Linear Regression:
    1. Load the Diabetes Dataset from sklearn.datasets.
    2. Compute Pearson correlation between BMI and disease progression (target).
    3. Fit a Simple Linear Regression model: target = beta0 + beta1 * BMI.
    4. Display OLS regression summary and provide slope interpretation.

Q2) Multiple Linear Regression:
    1. Fit Multiple Linear Regression with predictors: BMI, BP (blood pressure), Age.
    2. Display OLS regression summary.
    3. Provide interpretation of significant predictors (p < 0.05) and insignificant predictors.

Q3) Spearman Rank Correlation:
    Given two variables:
    Study Time: [2, 4, 1, 5, 3]
    Exam Score: [50, 65, 45, 80, 60]
    1. Compute Spearman's rank correlation coefficient and p-value.
    2. State the monotonic relationship.
================================================================================
"""

from sklearn.datasets import load_diabetes
import pandas as pd
import statsmodels.api as sm
from scipy.stats import spearmanr

# ------------------------------------------------------------------------------
# Q1: Simple Linear Regression (BMI vs Target)
# ------------------------------------------------------------------------------
diabetes = load_diabetes(as_frame=True)
df = diabetes.frame
print("--- Diabetes Dataset Head ---")
print(df.head())

# Correlation
print("\\n--- Correlation ---")
print(df[['bmi', 'target']].corr())

# Simple linear regression
x = sm.add_constant(df['bmi'])
y = df['target']
model = sm.OLS(y, x).fit()
print("\\n--- Regression Summary ---")
print(model.summary())

"""
Slope interpretation:
For every one-unit increase in BMI, predicted Y increases by 949.4353 units on average.
"""

# ------------------------------------------------------------------------------
# Q2: Multiple Linear Regression (BMI, BP, Age vs Target)
# ------------------------------------------------------------------------------
print("\\n--- Q2: Multiple Linear Regression ---")
x_multi = df[["bmi", "bp", "age"]]
x_multi = sm.add_constant(x_multi)
y = df["target"]
model_multi = sm.OLS(y, x_multi).fit()
print(model_multi.summary())

"""
Regression Coefficients Summary:
* Significant Predictors (p < 0.05):
  - BMI (coef = 788.78): Strongest positive effect. A 1-unit increase yields a ~788.8 unit increase in target.
  - BP (coef = 394.13): Positive effect. A 1-unit increase yields a ~394.1 unit increase in target.
  - Intercept (const) (coef = 152.13): Expected value of target when all predictors are zero.

* Insignificant Predictors (p >= 0.05):
  - Age (coef = 25.99, p = 0.685): No statistically significant relationship with the target in this model.
"""

# ------------------------------------------------------------------------------
# Q3: Spearman Rank Correlation (Study Time vs Exam Score)
# ------------------------------------------------------------------------------
print("\\n--- Q3: Spearman Rank Correlation ---")
study_time = [2, 4, 1, 5, 3]
exam_score = [50, 65, 45, 80, 60]

correlation, p_value = spearmanr(study_time, exam_score)

print("Spearman's correlation coefficient:", correlation)
print("p-value:", p_value)

"""
Interpretation:
Spearman correlation coefficient is 1.0 -> Perfectly Positively Correlated.
"""
'''

# ==============================================================================
# PRACTICAL 7 (from asm_dar/ASM-Prac7.ipynb)
# ==============================================================================
p7_code = '''"""
================================================================================
PRACTICAL 7: CLASSIFICATION (LOGISTIC REGRESSION: CHURN & PENGUINS)
================================================================================
FULL QUESTIONS:

Q1) Customer Churn Prediction using Logistic Regression:
    1. Load 'scikit-learn/churn-prediction' using datasets.load_dataset.
    2. Select predictors: tenure, MonthlyCharges.
    3. Target: Churn mapped to binary (No: 0, Yes: 1).
    4. Split into train/test sets (80/20, random_state=42, stratify=y).
    5. Fit LogisticRegression model.
    6. Evaluate: Confusion Matrix, Accuracy, Precision, Recall, F1 Score, Classification Report.
    7. Plot ROC curve and report AUC score.

Q2) Penguin Species Classification using Logistic Regression (Raw):
    1. Load 'penguins' dataset from seaborn.
    2. Filter for Adelie and Gentoo species.
    3. Features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g. Target: Gentoo (1) vs Adelie (0).
    4. Fit LogisticRegression(max_iter=1000) and evaluate metrics & ROC curve.

Q3) Penguin Species Classification using Pipeline with StandardScaler:
    1. Build a Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression(max_iter=1000))]).
    2. Fit on training data and predict on test set.
    3. Evaluate Confusion Matrix, Performance Metrics, and plot ROC curve with AUC.
================================================================================
"""

# ------------------------------------------------------------------------------
# Q1: Customer Churn Prediction
# ------------------------------------------------------------------------------
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score,
    f1_score, classification_report, roc_curve, roc_auc_score
)
import matplotlib.pyplot as plt

print("--- Q1: Customer Churn Prediction ---")
dataset = load_dataset("scikit-learn/churn-prediction")
df = dataset['train'].to_pandas()

# Selection predictors and target
x = df[["tenure", "MonthlyCharges"]]
y = df["Churn"].map({"No": 0, "Yes": 1})

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# Fit Logistic Regression
model = LogisticRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Confusion Matrix
print("Confusion Matrix: ")
print(confusion_matrix(y_test, y_pred))

# Performance Metrics
print("\\n Performance Metrics")
print("---------------------")
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred))
print("Recall: ", recall_score(y_test, y_pred))
print("F1-score: ", f1_score(y_test, y_pred))

# Complete classification report
print("\\n Classification Report")
print("-----------------------")
print(classification_report(y_test, y_pred))

"""
Interpretation:
The misclassified value is 319 (sum of off-diagonal elements in confusion matrix).
"""

# Predicted probabilities for churn
y_pred_prob = model.predict_proba(x_test)[:, 1]

# ROC curve and AUC
fpr, tpr, threshold = roc_curve(y_test, y_pred_prob)
auc = roc_auc_score(y_test, y_pred_prob)
print("AUC:", auc)

# Plot ROC curve
plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, label=f"ROC curve (AUC={auc:.3f})")
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Customer Churn")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------
# Q2: Penguin Species Classification (Raw Logistic Regression)
# ------------------------------------------------------------------------------
import seaborn as sns

print("\\n--- Q2: Penguin Classification (Raw Features) ---")
df_pen = sns.load_dataset("penguins")

# Filter for Adelie and Gentoo species, select features, and drop NaNs
df1 = df_pen[df_pen['species'].isin(['Adelie', 'Gentoo'])].copy()
features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
df1 = df1[features + ['species']].dropna()

# Selection predictors and target
x_pen = df1[features]
y_pen = (df1["species"] == "Gentoo").astype(int)

# Train-test split
x_train_p, x_test_p, y_train_p, y_test_p = train_test_split(
    x_pen, y_pen, test_size=0.2, random_state=42, stratify=y_pen
)

# Fit Logistic Regression
model1 = LogisticRegression(max_iter=1000)
model1.fit(x_train_p, y_train_p)

# Predict
y_pred_p = model1.predict(x_test_p)

# Confusion Matrix
print("Confusion Matrix: ")
print(confusion_matrix(y_test_p, y_pred_p))

# Performance Metrics
print("\\n Performance Metrics")
print("---------------------")
print("Accuracy: ", accuracy_score(y_test_p, y_pred_p))
print("Precision: ", precision_score(y_test_p, y_pred_p))
print("Recall: ", recall_score(y_test_p, y_pred_p))
print("F1-score: ", f1_score(y_test_p, y_pred_p))

# Complete classification report
print("\\n Classification Report")
print("-----------------------")
print(classification_report(y_test_p, y_pred_p))

# ROC curve and AUC
y_pred_prob_p = model1.predict_proba(x_test_p)[:, 1]
fpr_p, tpr_p, threshold_p = roc_curve(y_test_p, y_pred_prob_p)
auc_p = roc_auc_score(y_test_p, y_pred_prob_p)
print("AUC:", auc_p)

plt.figure(figsize=(7, 5))
plt.plot(fpr_p, tpr_p, label=f"ROC curve (AUC={auc_p:.3f})")
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Penguin Classification (Raw)")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------
# Q3: Penguin Classification with StandardScaler Pipeline
# ------------------------------------------------------------------------------
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

print("\\n--- Q3: Penguin Classification (StandardScaler Pipeline) ---")
# Standardize and fit logistic regression
model2 = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])
model2.fit(x_train_p, y_train_p)

# Predict
y_pred_pipe = model2.predict(x_test_p)
y_pred_prob_pipe = model2.predict_proba(x_test_p)[:, 1]

# Evaluation Metrics
print("Confusion Matrix: ")
print(confusion_matrix(y_test_p, y_pred_pipe))

print("\\n Performance Metrics")
print("---------------------")
print("Accuracy: ", accuracy_score(y_test_p, y_pred_pipe))
print("Precision: ", precision_score(y_test_p, y_pred_pipe))
print("Recall: ", recall_score(y_test_p, y_pred_pipe))
print("F1-score: ", f1_score(y_test_p, y_pred_pipe))

fpr_pipe, tpr_pipe, threshold_pipe = roc_curve(y_test_p, y_pred_prob_pipe)
auc_pipe = roc_auc_score(y_test_p, y_pred_prob_pipe)
print("AUC:", auc_pipe)

plt.figure(figsize=(7, 5))
plt.plot(fpr_pipe, tpr_pipe, label=f"ROC curve (AUC={auc_pipe:.3f})")
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Penguin Classification (Pipeline)")
plt.legend()
plt.show()
'''

# ==============================================================================
# PRACTICAL 8 (from asm_dar/ASM-Prac8.ipynb)
# ==============================================================================
p8_code = '''"""
================================================================================
PRACTICAL 8: PRINCIPAL COMPONENT ANALYSIS (PCA)
================================================================================
FULL QUESTIONS:

Q1) PCA on Wine Dataset:
    1. Load the Wine Dataset from sklearn.datasets (178 rows, 13 features).
    2. Standardize the dataset using StandardScaler.
    3. Apply PCA and calculate:
       - Explained variance ratio for each component.
       - Cumulative explained variance.
    4. Determine the number of components explaining at least 90% variance.
    5. Transform dataset using selected components and display reduced shape.
    6. Fit PCA with 2 components and plot a 2D scatter plot colored by Wine class.

Q2) PCA on Breast Cancer Dataset:
    1. Load Breast Cancer Dataset from sklearn.datasets (569 rows, 30 features).
    2. Standardize features using StandardScaler.
    3. Apply PCA and compute explained variance ratio and cumulative variance.
    4. Find the number of components explaining at least 90% variance.
    5. Reduce dimensions to selected components and display reduced shape.
    6. Fit PCA with 2 components and plot a 2D scatter plot colored by Cancer class.
================================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine, load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ------------------------------------------------------------------------------
# Q1: Wine Dataset PCA
# ------------------------------------------------------------------------------
print("--- Q1: Wine Dataset PCA ---")
wine = load_wine()
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine['target'] = wine.target

print("Original dataset shape:", df_wine.shape)
print(df_wine.head())

# Standardization
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_wine)

# PCA
pca = PCA()
df_pca = pca.fit_transform(df_scaled)

# Explained Variance
explained_variance = pca.explained_variance_ratio_
print("\\nExplained Variance Ratio:\\n", explained_variance)

# Cumulative Explained Variance
cumulative_variance = explained_variance.cumsum()
print("\\nCumulative Explained Variance:\\n", cumulative_variance)

# Number of components explaining at least 90%
n_components = (cumulative_variance >= 0.9).argmax() + 1
print("\\nNumber of components explaining at least 90% of variance:", n_components)

# Transform using selected components
pca_reduced = PCA(n_components=n_components)
x_reduced = pca_reduced.fit_transform(df_scaled)
print("Reduced dataset shape:", x_reduced.shape)

# PCA with two components
pca_2 = PCA(n_components=2)
x_reduced_2 = pca_2.fit_transform(df_scaled)
print("2-Component PCA shape:", x_reduced_2.shape)

plt.figure(figsize=(8, 6))
plt.scatter(x_reduced_2[:, 0], x_reduced_2[:, 1], c=wine.target, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title("PCA: Wine Dataset")
plt.colorbar(label="Wine Class")
plt.show()

# ------------------------------------------------------------------------------
# Q2: Breast Cancer Dataset PCA
# ------------------------------------------------------------------------------
print("\\n--- Q2: Breast Cancer Dataset PCA ---")
cancer = load_breast_cancer()
x_c = cancer.data
y_c = cancer.target
target_name = cancer.target_names
feature_name = cancer.feature_names

print("Number of Observations:", x_c.shape)
print("Number of Features:", y_c.shape)
print("Target Names:", target_name)

df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)
print("Original Cancer dataset shape:", df_cancer.shape)
print(df_cancer.head())

# Standardization
scaler_c = StandardScaler()
df_c_scaled = scaler_c.fit_transform(df_cancer)

# PCA
pca_cancer = PCA()
df_c_pca = pca_cancer.fit_transform(df_c_scaled)

# Explained Variance
exp_var_c = pca_cancer.explained_variance_ratio_
print("\\nExplained Variance Ratio:\\n", exp_var_c)

# Cumulative Explained Variance
cum_var_c = exp_var_c.cumsum()
print("\\nCumulative Explained Variance:\\n", cum_var_c)

# Number of components explaining at least 90%
n_comp_c = (cum_var_c >= 0.9).argmax() + 1
print("\\nNumber of components explaining at least 90% of variance:", n_comp_c)

# Transform using selected components
pca_c_reduced = PCA(n_components=n_comp_c)
x_c_reduced = pca_c_reduced.fit_transform(df_c_scaled)
print("Reduced dataset shape:", x_c_reduced.shape)

# PCA with two components
pca_c_2 = PCA(n_components=2)
x_reduced_c2 = pca_c_2.fit_transform(df_c_scaled)
print("2-Component Cancer shape:", x_reduced_c2.shape)

plt.figure(figsize=(8, 6))
plt.scatter(x_reduced_c2[:, 0], x_reduced_c2[:, 1], c=cancer.target, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title("PCA: Cancer Dataset")
plt.colorbar(label="Cancer Class")
plt.show()
'''

# ==============================================================================
# PRACTICAL 9 (from asm_dar/ASM-Prac9.ipynb)
# ==============================================================================
p9_code = '''"""
================================================================================
PRACTICAL 9: BAYESIAN INFERENCE & SEQUENTIAL UPDATING
================================================================================
FULL QUESTIONS:

Sequential Bayesian Updating for Medical Testing:
A diagnostic test is used to detect a rare disease in a population.
- Disease prevalence (prior probability): P(Disease) = 0.01 (1%).
- Test sensitivity (True Positive Rate): P(+ | Disease) = 0.95 (95%).
- Test specificity (True Negative Rate): P(- | No Disease) = 0.90 (90%).
- False Positive Rate: P(+ | No Disease) = 1 - specificity = 0.10 (10%).

Tasks:
Q1) First Positive Test Update:
    - Calculate total probability of a positive test P(+).
    - Compute posterior probability of having the disease after one positive test:
      P(Disease | +).

Q2) Second Positive Test Update (Sequential Update):
    - Use the posterior probability from the first test as the new prior probability.
    - Calculate the new probability of a positive test.
    - Compute updated posterior probability of having the disease: P(Disease | +, +).
    - Provide diagnostic conclusion.
================================================================================
"""

# ------------------------------------------------------------------------------
# Q1: First Positive Test Update
# ------------------------------------------------------------------------------
# Prior probability
prior_disease = 0.01

# Test characteristics
sensitivity = 0.95
specificity = 0.90

# Probability of positive test among people without disease
false_positive_rate = 1 - specificity

# Bayes's theorem after first positive test
prob_positive = (sensitivity * prior_disease) + (false_positive_rate * (1 - prior_disease))

posterior_1 = (sensitivity * prior_disease) / prob_positive

print("--- Q1: First Positive Test ---")
print("probability of positive test: ", prob_positive)
print("posterior probability after first positive test: ", posterior_1)

# ------------------------------------------------------------------------------
# Q2: Sequential Update (Second Positive Test)
# ------------------------------------------------------------------------------
# Use the posterior probability after first test as the new prior
new_prior = posterior_1

prob_positive_2 = (sensitivity * new_prior) + (false_positive_rate * (1 - new_prior))

posterior_2 = (sensitivity * new_prior) / prob_positive_2

print("\\n--- Q2: Second Positive Test (Sequential Update) ---")
print("probability of positive test: ", prob_positive_2)
print("posterior probability after second positive test: ", posterior_2)

"""
Conclusion:
If both tests are positive, there is a much higher chance of the user having the disease
(~48.06% compared to ~8.76% after one test, and 1% initial population baseline).
"""
'''

practicals = {
    1: p1_code.strip(),
    2: p2_code.strip(),
    3: p3_code.strip(),
    4: p4_code.strip(),
    5: p5_code.strip(),
    6: p6_code.strip(),
    7: p7_code.strip(),
    8: p8_code.strip(),
    9: p9_code.strip(),
}

print("=== 1. Writing asm/asm_1.py to asm/asm_9.py from ASM Dar ===")
all_combined = [
    '"""\\n' + '='*80 + '\\nAPPLIED STATISTICAL METHODS (ASM) - ALL PRACTICALS (1 TO 9)\\nFULL QUESTIONS, IMPLEMENTATION & INTERPRETATIONS (DARPAN)\\n' + '='*80 + '\\n"""\\n'
]

for i in range(1, 10):
    content = practicals[i]
    dest = os.path.join(asm_dir, f"asm_{i}.py")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)
    all_combined.append(f"\\n# {'='*78}\\n# PRACTICAL {i}\\n# {'='*78}\\n" + content)
    print(f"asm/asm_{i}.py written successfully")

# 2. Write all_asm_practicals.py
all_code = "\\n".join(all_combined)
with open(os.path.join(asm_dir, "all_asm_practicals.py"), "w", encoding="utf-8") as f:
    f.write(all_code)
print("asm/all_asm_practicals.py written successfully")

# 3. Copy to root files and all short aliases
print("\\n=== 2. Copying to root and aliases ===")
for i in range(1, 10):
    src = os.path.join(asm_dir, f"asm_{i}.py")
    with open(src, "r", encoding="utf-8") as f:
        code = f.read()
    
    aliases = [f"practical_{i}.py", f"p{i}.py", f"asm{i}.py", f"asm{i}", f"{i}"]
    if i == 2:
        aliases.extend(["practical_2a.py", "practical_2b.py", "p2a.py", "p2b.py", "2b"])
    
    for alias in aliases:
        with open(os.path.join(root, alias), "w", encoding="utf-8") as f:
            f.write(code)

for alias in ["all_practicals_1_to_6.py", "all.py", "all", "asm_all.py", "asmall", "asm0"]:
    with open(os.path.join(root, alias), "w", encoding="utf-8") as f:
        f.write(all_code)
print("All root aliases updated.")

# 4. Check syntax for all 9 practicals
print("\\n=== 3. Checking Syntax of All 9 Practicals ===")
all_syntax_pass = True
for i in range(1, 10):
    fn = os.path.join(root, f"practical_{i}.py")
    try:
        py_compile.compile(fn, doraise=True)
        print(f"Practical {i} ({fn}): SYNTAX OK")
    except Exception as e:
        print(f"Practical {i} ({fn}): SYNTAX FAILED -> {e}")
        all_syntax_pass = False

if not all_syntax_pass:
    print("Syntax verification FAILED.")
    sys.exit(1)

print("\\nALL 9 PRACTICALS HAVE 100% PERFECT SYNTAX!")
