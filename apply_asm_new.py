import os

root = r'c:\Users\asdf\Downloads\MSc_BDA_AL-'
asm_dir = os.path.join(root, 'asm')

# ==============================================================================
# ASM PRACTICAL 1 (from asm new/practical1.py)
# ==============================================================================
p1_code = '''"""
================================================================================
PRACTICAL 1: DESCRIPTIVE STATISTICS & EXPLORATORY DATA ANALYSIS (EDA)
================================================================================
FULL QUESTIONS:

Q1) Analyze the Iris Dataset:
    1. Load the Iris Dataset (150 rows, 4 numerical features).
    2. Calculate Mean, Median, Mode(s), Standard Deviation, Variance, Skewness, Kurtosis
       for each numerical feature.
    3. Plot distribution histograms with KDE for all numerical features.
    4. Provide detailed feature-by-feature statistical interpretation.

Q2) Analyze the Tips Dataset:
    1. Load the Tips Dataset (244 rows, 7 columns).
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for numerical features (total_bill, tip, size).
    3. Plot histograms with KDE for numerical features.
    4. Provide statistical interpretation of customer billing & tipping behavior.

Q3) Analyze the Indian Stock Market Dataset:
    1. Load 'indian_stock_market.csv' (2306 rows).
    2. Calculate summary statistics for numerical stock prices (MSFT, IBM, SBUX, AAPL, GSPC).
    3. Plot distribution histograms with KDE in a 3x2 grid.
================================================================================
"""

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
print("\n--- Iris Dataset Info ---")
iris.info()

numerical_cols = iris.select_dtypes(include=np.number).columns.tolist()

for col in numerical_cols:
    mean_val = iris[col].mean()
    median_val = iris[col].median()
    mode_val = iris[col].mode().tolist() # mode() can return multiple values
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
    print(f" Kurtosis: {kurtosis_val:.3f}")
    print("\n")

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
print("--- Tips Dataset Head ---")
print(tips.head())
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
    print(f"Kurtosis: {kurtosis_val:.3f}\n")

"""
Q2 Interpretation:
1. Total Bill: Right-skewed distribution (skewness 1.133). Most bills are small, but high-end bills pull the mean (19.786) above the median (17.795).
2. Tip: High kurtosis (3.648) shows concentration around $2-$3, with a round-number mode of exactly $2.00.
3. Party Size: Discrete integers peaking at parties of two (mode = 2, median = 2).
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
df = pd.read_csv('indian_stock_market.csv')

numerical_cols = df.select_dtypes(include=np.number).columns.to_list()

for col in numerical_cols:
    mean_val = df[col].mean()
    median_val = df[col].median()
    mode_val = df[col].mode().tolist()
    std_val = df[col].std()
    var_val = df[col].var()
    skew_val = skew(df[col].dropna(), nan_policy='omit')
    kurtosis_val = kurtosis(df[col].dropna(), nan_policy='omit')

    print(f"----- Stats for '{col}' -----")
    print(f"Mean: {mean_val:.3f}")
    print(f"Median: {median_val:.3f}")
    print(f"Mode: {mode_val}")
    print(f"Standard Deviation: {std_val:.3f}")
    print(f"Variance: {var_val:.3f}")
    print(f"Skewness: {skew_val:.3f}")
    print(f"Kurtosis: {kurtosis_val:.3f}\n")

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(3, 2, i + 1)
    sns.histplot(df[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
'''

# ==============================================================================
# ASM PRACTICAL 2 (from asm new/asm_pract2.py)
# ==============================================================================
p2_code = '''"""
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
'''

# ==============================================================================
# ASM PRACTICAL 3 (from asm new/ASM_Pract3.ipynb)
# ==============================================================================
p3_code = '''"""
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

print("\nBootstrap Mean =", np.mean(bootstrap_mean))
print("95% Bootstrap CI =", (lower_bootstrap, upper_bootstrap))

# ------------------------------------------------------------------------------
# Comparison
# ------------------------------------------------------------------------------
print("\nt-based CI =", (lower, upper))
print("bootstrap CI =", (lower_bootstrap, upper_bootstrap))
print("t-based CI width =", upper - lower)
print("bootstrap CI width =", upper_bootstrap - lower_bootstrap)
'''

# ==============================================================================
# ASM PRACTICAL 4 (from asm new/asm_pract4.py)
# ==============================================================================
p4_code = '''"""
================================================================================
PRACTICAL 4: HYPOTHESIS TESTING (T-TEST, CHI-SQUARE, ONE-WAY ANOVA & TUKEY HSD)
================================================================================
FULL QUESTIONS:

Question 1: (Two-Sample Independent t-Test)
    Using the Titanic dataset, perform Welch's independent two-sample t-test
    (equal_var=False) to test whether ticket fares paid by male vs female passengers differ.
    H0: The mean fare paid by male and female passengers differs insignificantly.
    H1: The mean fare paid by male and female passengers differs significantly.

Question 2: (Chi-Square Test of Independence)
    Using the Titanic dataset, construct a contingency table crossing passenger
    'class' (First, Second, Third) with 'survived' status (0, 1).
    Perform a Chi-Square test of independence to assess whether passenger class
    is significantly associated with survival outcome.
    H0: Passenger class and survival status are not associated.
    H1: Passenger class and survival status are associated.

Question 3: (One-Way ANOVA & Post-Hoc Tukey HSD Test)
    H0: Mean fares do not differ significantly across the three passenger classes.
    1. Perform One-Way ANOVA (f_oneway).
    2. Conduct Tukey's Honestly Significant Difference (HSD) test to identify
       which specific pairs of passenger classes differ in mean fare.
================================================================================
"""

import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ------------------------------------------------------------------------------
# Q1: Two-Sample Independent t-test
# ------------------------------------------------------------------------------
print("H0: The mean fare paid by male and female passengers differs insignificantly.")
print("H1: The mean fare paid by male and female passengers differs significantly.")

df = sns.load_dataset("titanic")

male = df[df["sex"] == "male"]["fare"].dropna()
female = df[df["sex"] == "female"]["fare"].dropna()

t_stat, p_value = stats.ttest_ind(
    male, female, equal_var=False
)

print("\nt-statistic:", t_stat)
print("p_value:", p_value)

# ------------------------------------------------------------------------------
# Q2: Chi-Square Test of Independence
# ------------------------------------------------------------------------------
print("\n" + "="*50)
print("H0: Passenger class and survival status are not associated.")
print("H1: Passenger class and survival status are associated.")

table = pd.crosstab(df["class"], df["survived"])
print("\nContingency Table:")
print(table)

chi2, p_value, dof, expected = chi2_contingency(table)

print("\nchi-square statistic:", chi2)
print("Degrees of freedom:", dof)
print("p_value:", p_value)

# ------------------------------------------------------------------------------
# Q3: One-Way ANOVA & Post-Hoc Tukey HSD
# ------------------------------------------------------------------------------
print("\n" + "="*50)
print("One-Way ANOVA across Passenger Classes:")

first = df[df["class"] == "First"]["fare"].dropna()
second = df[df["class"] == "Second"]["fare"].dropna()
third = df[df["class"] == "Third"]["fare"].dropna()

F, p_value = f_oneway(first, second, third)

print("F-statistic:", F)
print("p_value:", p_value)

print("\nTukey HSD Post-Hoc Test:")
df_clean = df.dropna(subset=["fare"])
tukey = pairwise_tukeyhsd(endog=df_clean["fare"], groups=df_clean["class"])
print(tukey)

"""
Interpretation:
First and Second & First and Third mean fares differ significantly (reject=True).
Second and Third fares do not differ significantly (reject=False, p-adj = 0.108).
"""
'''

# ==============================================================================
# ASM PRACTICAL 5 (from asm new/ASM_Pract5,ipynb.ipynb)
# ==============================================================================
p5_code = '''"""
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
print("H1: Means for both groups are not same.\n")

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
    print("\nDecision: Reject H0 -> The means of both groups differ significantly.")
else:
    print("\nDecision: Fail to reject H0 -> The means of both groups do not differ significantly.")
'''

# ==============================================================================
# ASM PRACTICAL 6 (from asm new/ASM-Pract6.ipynb - Colab.pdf)
# ==============================================================================
p6_code = '''"""
================================================================================
PRACTICAL 6: LINEAR REGRESSION & SPEARMAN CORRELATION
================================================================================
FULL QUESTIONS:

Q1) Simple Linear Regression:
    Load the scikit-learn Diabetes dataset into a pandas DataFrame.
    1. Evaluate the Pearson linear correlation between Body Mass Index ('bmi') and disease progression ('target').
    2. Fit an Ordinary Least Squares (OLS) Simple Linear Regression model (target ~ bmi + intercept) using statsmodels.
    3. Formulate the regression equation and calculate R-squared.

Q2) Multiple Linear Regression:
    Fit an OLS Multiple Linear Regression model predicting disease progression ('target')
    using three predictors: 'bmi', blood pressure ('bp'), and 'age'.
    Evaluate:
    - R-squared and Adjusted R-squared.
    - Which individual predictors are statistically significant.
    - Write down the Multiple Linear Regression equation.

Q3) Spearman Rank Correlation:
    Given:
    study_time = [2, 4, 1, 5, 3]
    exam_score = [50, 65, 45, 80, 60]
    Calculate the Spearman rank correlation coefficient and p-value.
    Interpret the relationship.
================================================================================
"""

from sklearn.datasets import load_diabetes
import pandas as pd
import statsmodels.api as sm
from scipy.stats import spearmanr

# ------------------------------------------------------------------------------
# Q1: Simple Linear Regression
# ------------------------------------------------------------------------------
diabetes = load_diabetes(as_frame=True)
df = diabetes.frame
print("--- Diabetes Dataset Head ---")
print(df.head())

# Correlation
print("\n--- Pearson Correlation: BMI vs Target ---")
print(df[["bmi", "target"]].corr())

# Simple linear regression
X = sm.add_constant(df["bmi"])
y = df["target"]
model = sm.OLS(y, X).fit()
print("\n--- Simple OLS Model Summary ---")
print(model.summary())

"""
Q1 Ans:
Pearson Correlation: r = 0.5865
There is a moderate positive relationship between BMI and disease progression.
Regression Equation: Y = 152.1335 + 949.4353 * (BMI)
R^2 = 0.3439
Therefore, BMI explains 34.39% of the variation in disease progression.
"""

# ------------------------------------------------------------------------------
# Q2: Multiple Linear Regression
# ------------------------------------------------------------------------------
X_multi = df[["bmi", "bp", "age"]]
X_multi = sm.add_constant(X_multi)
model_multi = sm.OLS(df["target"], X_multi).fit()
print("\n--- Multiple OLS Model Summary ---")
print(model_multi.summary())

"""
Q2 Ans:
R^2 = 0.396, Adjusted R^2 = 0.392
Significant Predictors:
- BMI -> Significant (p < 0.001)
- BP  -> Significant (p < 0.001)
- Age -> Not Significant (p = 0.685)
Regression Equation:
Y = 152.1335 + 788.7827(BMI) + 394.1271(BP) + 25.9904(Age)
Conclusion:
BMI and BP are significant predictors of disease progression, while Age is not significant.
"""

# ------------------------------------------------------------------------------
# Q3: Spearman Rank Correlation
# ------------------------------------------------------------------------------
study_time = [2, 4, 1, 5, 3]
exam_score = [50, 65, 45, 80, 60]
correlation, p_value = spearmanr(study_time, exam_score)

print("\n--- Spearman Rank Correlation ---")
print("Spearman's correlation coefficient:", correlation)
print("p-value:", p_value)

"""
Q3 Ans:
Study Time & Exam score are perfectly positively correlated (rho = 1.0, p = 1.40e-24).
"""
'''

# ==============================================================================
# ASM PRACTICAL 7 (from asm new/ASM_Pract7chirag.ipynb - Colab.pdf)
# ==============================================================================
p7_code = '''"""
================================================================================
PRACTICAL 7: LOGISTIC REGRESSION & CLASSIFICATION METRICS
================================================================================
FULL QUESTIONS:

Q1) Customer Churn Prediction using Logistic Regression:
    1. Load dataset 'scikit-learn/churn-prediction'.
    2. Select predictors 'tenure' and 'MonthlyCharges', target 'Churn' (No=0, Yes=1).
    3. Split into train and test sets (80-20 stratified split).
    4. Fit Logistic Regression model and predict on test set.
    5. Evaluate model with Confusion Matrix, Accuracy, Precision, Recall, F1-Score,
       and complete Classification Report.
    6. Plot ROC Curve and compute AUC score.

Q2) Penguin Species Classification using Logistic Regression:
    1. Load Palmer Penguins dataset and filter for species 'Adelie' and 'Gentoo'.
    2. Use predictors: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g.
    3. Standardize and fit Logistic Regression within an ML Pipeline.
    4. Evaluate model with Confusion Matrix, Performance Metrics, Classification Report,
       and ROC Curve with AUC score.
================================================================================
"""

# ------------------------------------------------------------------------------
# Q1: Customer Churn Prediction
# ------------------------------------------------------------------------------
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report,
    roc_curve, roc_auc_score
)
import matplotlib.pyplot as plt

# Load dataset
dataset = load_dataset("scikit-learn/churn-prediction")
df = dataset["train"].to_pandas()

# Select predictors and target
X = df[["tenure", "MonthlyCharges"]]
y = df["Churn"].map({"No": 0, "Yes": 1})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Fit Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Performance Metrics
print("\nPerformance Metrics:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ROC Curve and AUC
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)
print("AUC:", auc)

plt.plot(fpr, tpr, label=f"ROC Curve (AUC={auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Customer Churn")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------
# Q2: Penguin Species Classification Pipeline
# ------------------------------------------------------------------------------
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load dataset
df_peng = sns.load_dataset("penguins")

# Select Adelie and Gentoo species
df_peng = df_peng[df_peng["species"].isin(["Adelie", "Gentoo"])].copy()

# Select predictors
features = [
    "bill_length_mm", "bill_depth_mm",
    "flipper_length_mm", "body_mass_g"
]
df_peng = df_peng[features + ["species"]].dropna()
X = df_peng[features]
y = (df_peng["species"] == "Gentoo").astype(int)
print("\nDataset Shape:", df_peng.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardize and fit Logistic Regression
modelb = Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression(max_iter=1000))
])
modelb.fit(X_train, y_train)

# Make predictions
y_pred = modelb.predict(X_test)

# Confusion Matrix & Performance Metrics
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nPerformance Metrics:")
print("--------------------")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ROC Curve and AUC
y_prob = modelb.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)
print("AUC:", auc)

plt.plot(fpr, tpr, label=f"ROC Curve (AUC={auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Penguin Species Classification")
plt.legend()
plt.show()
'''

# ==============================================================================
# ASM PRACTICAL 8 (from asm new/Prac8.ipynb - Colab.pdf)
# ==============================================================================
p8_code = '''"""
================================================================================
PRACTICAL 8: PRINCIPAL COMPONENT ANALYSIS (PCA)
================================================================================
FULL QUESTIONS:

Q1 & Q2) PCA on Wine Dataset:
    1. Load the Wine dataset (178 rows, 13 features).
    2. Standardize features with StandardScaler.
    3. Apply PCA and compute the Explained Variance Ratio and Cumulative Explained Variance.
    4. Find the number of principal components explaining at least 90% variance.
    5. Transform dataset with PCA (n_components=2) and plot 2D scatter plot colored by wine class.

Q3) PCA on Breast Cancer Dataset:
    1. Load the Breast Cancer dataset (569 observations, 30 features).
    2. Standardize all 30 features using StandardScaler.
    3. Apply PCA and determine the minimum number of components explaining at least 90% variance.
    4. Output the reduced dataset shape.
================================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine, load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ------------------------------------------------------------------------------
# Q1 & Q2: Wine Dataset PCA
# ------------------------------------------------------------------------------
wine = load_wine()
x = pd.DataFrame(data=wine.data, columns=wine.feature_names)
y = wine.target

print("Original dataset shape:", x.shape)
print("First five observations:\n", x.head())

# Standardization
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Applying PCA
pca = PCA()
x_pca = pca.fit_transform(x_scaled)

# Explained variance
explained_variance = pca.explained_variance_ratio_
print("\nExplained variance ratio:\n", explained_variance)

# Cumulative explained variance
cumulative_variance = explained_variance.cumsum()
print("\nCumulative explained variance:\n", cumulative_variance)

# Number of components explaining at least 90%
n_components = (cumulative_variance >= 0.9).argmax() + 1
print("\nNumber of components explaining at least 90% variance:", n_components)

# Transform using selected components
pca_reduced = PCA(n_components=n_components)
x_reduced = pca_reduced.fit_transform(x_scaled)
print("Reduced dataset shape:", x_reduced.shape)

# PCA with two components for visualization
pca_2 = PCA(n_components=2)
x_pca_2 = pca_2.fit_transform(x_scaled)
print("2D PCA shape:", x_pca_2.shape)

plt.figure(figsize=(8, 6))
plt.scatter(x_pca_2[:, 0], x_pca_2[:, 1], c=y)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA of Wine Dataset')
plt.colorbar(label="Wine Class")
plt.show()

# ------------------------------------------------------------------------------
# Q3: Breast Cancer Dataset PCA
# ------------------------------------------------------------------------------
cancer = load_breast_cancer()
x = cancer.data
y = cancer.target
target_names = cancer.target_names
feature_names = cancer.feature_names

print("\n" + "="*50)
print("Breast Cancer Dataset:")
print("Number of observations:", x.shape[0])
print("Number of Features:", x.shape[1])
print("Target names:", target_names)

# Standardization
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Applying PCA
pca = PCA()
x_pca = pca.fit_transform(x_scaled)

# Explained variance
explained_variance = pca.explained_variance_ratio_
print("\nExplained variance ratio:\n", explained_variance)

# Cumulative explained variance
cumulative_variance = explained_variance.cumsum()
print("\nCumulative explained variance:\n", cumulative_variance)

# Number of components explaining at least 90%
n_components = (cumulative_variance >= 0.9).argmax() + 1
print("\nNumber of components explaining at least 90% variance:", n_components)

# Transform using selected components
pca_reduced = PCA(n_components=n_components)
x_reduced = pca_reduced.fit_transform(x_scaled)
print("Reduced dataset shape:", x_reduced.shape)
'''

# ==============================================================================
# ASM PRACTICAL 9 (from asm new/prac9 (1).ipynb)
# ==============================================================================
p9_code = '''"""
================================================================================
PRACTICAL 9: BAYESIAN UPDATING FOR MEDICAL DIAGNOSTIC TESTING
================================================================================
FULL QUESTIONS:

Question: (Sequential Bayesian Updating for Medical Diagnostic Testing)
    A diagnostic medical test has the following characteristics:
    - Prior probability of disease: P(Disease) = 0.01 (1%)
    - Test Sensitivity: P(+ | Disease) = 0.95 (95%)
    - Test Specificity: P(- | No Disease) = 0.90 (90%)
    - False Positive Rate: P(+ | No Disease) = 1 - Specificity = 0.10 (10%)

    1. Calculate total probability of a positive test: P(+).
    2. Compute the Posterior Probability after the FIRST positive test.
    3. Use the first posterior as the NEW PRIOR and compute the Posterior Probability
       after a SECOND independent positive test!
================================================================================
"""

# Bayesian Updating for Medical Testing

# Prior probability
prior_disease = 0.01

# Test characteristics
sensitivity = 0.95
specificity = 0.90
false_positive_rate = 1 - specificity

# Probability of a positive test among people without disease
prob_positive = (
    sensitivity * prior_disease + false_positive_rate * (1 - prior_disease)
)

posterior_1 = (
    sensitivity * prior_disease
) / prob_positive

print("Probability of a positive test:", prob_positive)
print("Posterior probability after first positive test:", posterior_1)

# ------------------------------------------------------------------------------
# Sequential Bayesian Updating (Second Positive Test)
# ------------------------------------------------------------------------------
# Use posterior probability after first test as new prior!
new_prior = posterior_1

prob_positive_2 = (
    sensitivity * new_prior + false_positive_rate * (1 - new_prior)
)

posterior_2 = (
    sensitivity * new_prior
) / prob_positive_2

print("\n--- Summary of Sequential Bayesian Tests ---")
print("Posterior probability after FIRST positive test :", posterior_1)
print("Posterior probability after SECOND positive test:", posterior_2)
'''

all_practicals = [
    (1, p1_code),
    (2, p2_code),
    (3, p3_code),
    (4, p4_code),
    (5, p5_code),
    (6, p6_code),
    (7, p7_code),
    (8, p8_code),
    (9, p9_code),
]

# Write individual files to asm/
for num, code in all_practicals:
    path = os.path.join(asm_dir, f'asm_{num}.py')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code.strip() + '\n')
    print(f'Wrote asm/asm_{num}.py')

# Combine all into all_asm_practicals.py
combined_header = '"""\n' + '='*80 + '\nAPPLIED STATISTICAL METHODS (ASM) - PRACTICALS 1 TO 9\nDITTO QUESTIONS, CODE & INTERPRETATIONS FROM ASM NEW\n' + '='*80 + '\n"""\n'
combined_body = '\n\n'.join([f"# {'='*78}\n# PRACTICAL {num}\n# {'='*78}\n" + code.strip() for num, code in all_practicals])
combined_full = combined_header + '\n' + combined_body + '\n'

with open(os.path.join(asm_dir, 'all_asm_practicals.py'), 'w', encoding='utf-8') as f:
    f.write(combined_full)
print('Wrote asm/all_asm_practicals.py')

# Sync to root files so curl delivers the new ditto versions!
for num, code in all_practicals:
    clean_code = code.strip() + '\n'
    for dst in [f'practical_{num}.py', f'p{num}.py', f'asm{num}.py', f'asm{num}', f'{num}']:
        with open(os.path.join(root, dst), 'w', encoding='utf-8') as f:
            f.write(clean_code)
    if num == 2:
        for dst in ['practical_2a.py', 'practical_2b.py', 'p2a.py', 'p2b.py', '2b']:
            with open(os.path.join(root, dst), 'w', encoding='utf-8') as f:
                f.write(clean_code)

for dst in ['all_practicals_1_to_6.py', 'all.py', 'all', 'asm_all.py', 'asmall', 'asm0']:
    with open(os.path.join(root, dst), 'w', encoding='utf-8') as f:
        f.write(combined_full)

print('All root files synchronized successfully!')
