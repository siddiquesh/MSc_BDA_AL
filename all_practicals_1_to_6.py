"""
================================================================================
APPLIED STATISTICAL METHODS (ASM) - PRACTICALS 1 TO 9
FULL QUESTIONS & IMPLEMENTATION
================================================================================
"""


# ==============================================================================
# ASM PRACTICAL 1
# ==============================================================================
"""
================================================================================
PRACTICAL 1: DESCRIPTIVE STATISTICS & EXPLORATORY DATA ANALYSIS (EDA)
================================================================================
FULL QUESTIONS:

Q1) Analyze the Iris Dataset:
    1. Load the Iris Dataset.
    2. Calculate mean of each numerical feature.
    3. Calculate median of each numerical feature.
    4. Calculate mode(s) of each numerical feature.
       (Note: Mode can be multi-modal or cannot be calculated for continuous data)
    5. Calculate standard deviation of each numerical feature.
    6. Calculate variance of each numerical feature.
    7. Calculate skewness of each numerical feature.
    8. Calculate kurtosis of each numerical feature.
    9. Plot the distribution (histogram with KDE) for each numerical feature.
    10. Interpret the results.

Q2) Analyze the Tips Dataset:
    1. Load the Tips Dataset.
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for all numerical features (total_bill, tip, size).
    3. Plot histograms with KDE for numerical features.
    4. Interpret the results.

Q3) Analyze the Indian Stock Market Dataset:
    1. Load 'indian_stock_market.csv'.
    2. Calculate summary statistics (Mean, Median, Mode, Std Dev, Variance, Skewness, Kurtosis)
       for numerical stock prices (MSFT, IBM, SBUX, AAPL, GSPC).
    3. Plot distribution histograms with KDE.
    4. Interpret the results.
================================================================================
"""

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew,kurtosis
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())
iris.info()

numerical_cols = iris.select_dtypes(include=np.number).columns.to_list()
for col in numerical_cols:
  mean_val = iris[col].mean()
  median_val = iris[col].median()
  mode_val = iris[col].mode().tolist()
  std_val = iris[col].std()
  var_val = iris[col].var()
  skewness_val = skew(iris[col])
  kurtosis_val = kurtosis(iris[col])
  print(f"---Stats for {col}---")
  print(f" Mean: {mean_val}")
  print(f" Median: {median_val}")
  print(f" Mode: {mode_val}")
  print(f" Standard Deviation: {std_val}")
  print(f" Variance: {var_val}")
  print(f" Skewness: {skewness_val}")
  print(f" Kurtosis: {kurtosis_val}")
  print("\n")

plt.figure(figsize=(15,10))
for i, col in enumerate(numerical_cols):
  plt.subplot(2,2,i+1)
  sns.histplot(iris[col],kde=True,bins=15)
  plt.title(f'Distribution of {col}')
  plt.xlabel('col')
  plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Q2) Analyze the Tips dataset

tips = sns.load_dataset('tips')
print(tips.head())
tips.info()

numerical_cols = tips.select_dtypes(include=np.number).columns.to_list()
for col in numerical_cols:
  mean_val = tips[col].mean()
  median_val = tips[col].median()
  mode_val = tips[col].mode().tolist()
  std_val = tips[col].std()
  var_val = tips[col].var()
  skewness_val = skew(tips[col])
  kurtosis_val = kurtosis(tips[col])
  print(f"---Stats for {col}---")
  print(f" Mean: {mean_val}")
  print(f" Median: {median_val}")
  print(f" Mode: {mode_val}")
  print(f" Standard Deviation: {std_val}")
  print(f" Variance: {var_val}")
  print(f" Skewness: {skewness_val}")
  print(f" Kurtosis: {kurtosis_val}")
  print("\n")

plt.figure(figsize=(15,10))
for i, col in enumerate(numerical_cols):
  plt.subplot(2,2,i+1)
  sns.histplot(tips[col],kde=True,bins=15)
  plt.title(f'Distribution of {col}')
  plt.xlabel('col')
  plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Q3) Analyze the Stock dataset

import pandas as pd
stock = pd.read_csv('indian_stock_market.csv')
print(stock.head())
stock.info()

numerical_cols = stock.select_dtypes(include=np.number).columns.to_list()
for col in numerical_cols:
  mean_val = stock[col].mean()
  median_val = stock[col].median()
  mode_val = stock[col].mode().tolist()
  std_val = stock[col].std()
  var_val = stock[col].var()
  skewness_val = skew(stock[col])
  kurtosis_val = kurtosis(stock[col])
  print(f"---Stats for {col}---")
  print(f" Mean: {mean_val}")
  print(f" Median: {median_val}")
  print(f" Mode: {mode_val}")
  print(f" Standard Deviation: {std_val}")
  print(f" Variance: {var_val}")
  print(f" Skewness: {skewness_val}")
  print(f" Kurtosis: {kurtosis_val}")
  print("\n")

plt.figure(figsize=(15, 15))
for i, col in enumerate(numerical_cols):
   plt.subplot(3, 2, i + 1)
   sns.histplot(stock[col], kde=True, bins=15)
   plt.title(f'Distribution of {col}')
   plt.xlabel(col)
   plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ==============================================================================
# ASM PRACTICAL 2
# ==============================================================================
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

# ==============================================================================
# ASM PRACTICAL 3
# ==============================================================================
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

# ==============================================================================
# ASM PRACTICAL 4
# ==============================================================================
"""
================================================================================
PRACTICAL 4: HYPOTHESIS TESTING (T-TEST, CHI-SQUARE, ONE-WAY ANOVA & TUKEY HSD)
================================================================================
FULL QUESTIONS:

Question 1: (Two-Sample Independent t-Test)
    Using the Titanic dataset, perform Welch's independent two-sample t-test
    (equal_var=False) to test if there is a statistically significant difference
    between ticket fares paid by male passengers vs female passengers.
    H0: Mean fare of male = Mean fare of female.

Question 2: (Chi-Square Test of Independence)
    Using the Titanic dataset, construct a contingency table crossing passenger
    'class' (First, Second, Third) with 'survived' status (0, 1).
    Perform a Chi-Square test of independence to assess whether passenger class
    is significantly associated with survival outcome.

Question 3: (One-Way ANOVA & Post-Hoc Tukey HSD Test)
    Test the hypothesis:
    H0: Mean ticket fares do not differ significantly across the 3 passenger classes
        (First, Second, Third).
    1. Perform One-Way ANOVA (f_oneway).
    2. If p < 0.05, perform Tukey's Honestly Significant Difference (HSD) test
       to identify which specific pairwise passenger classes differ in mean fare.
================================================================================
"""

import seaborn as sns
from scipy import stats

df = sns.load_dataset("titanic")
male = df[df["sex"] == "male"]["fare"].dropna()
female = df[df["sex"] == "female"]["fare"].dropna()

t_stat, p_value = stats.ttest_ind(
    male, female, equal_var=False
)
print("t_statistic:", t_stat)
print("p-value:", p_value)

# Question 2: Chi-Square Test of Independence
from scipy.stats import chi2_contingency
import pandas as pd

table = pd.crosstab(df["class"], df["survived"])
print(table)

chi2, p_value, dof, expected = chi2_contingency(table)
print("Chi-square statistics:", chi2)
print("Degrees of Freedom:", dof)
print("p-value:", p_value)

# Question 3: One-Way ANOVA & Tukey HSD
# h0: mean fares do not differ significance across 3 passenger classes
from scipy.stats import f_oneway

first = df[df["class"] == "First"]["fare"].dropna()
second = df[df["class"] == "Second"]["fare"].dropna()
third = df[df["class"] == "Third"]["fare"].dropna()

F, p_value = f_oneway(first, second, third)
print("F-statistic:", F)
print("p-value:", p_value)

from statsmodels.stats.multicomp import pairwise_tukeyhsd

df = df.dropna(subset=["fare"])
tukey = pairwise_tukeyhsd(endog=df["fare"], groups=df["class"])
print(tukey)

# ==============================================================================
# ASM PRACTICAL 5
# ==============================================================================
"""
================================================================================
PRACTICAL 5: A/B TESTING
================================================================================
FULL QUESTIONS:

Question: (A/B Testing Analysis with Two-Sample Welch's t-Test)
    Given conversion / performance metrics from an A/B test with 20 users per group:
    - Control Group A:
      [42, 38, 45, 51, 47, 39, 44, 50, 46, 41, 43, 48, 37, 49, 45, 40, 52, 44, 46, 43]
    - Treatment Variant Group B:
      [48, 52, 55, 49, 58, 51, 54, 56, 50, 53, 57, 49, 55, 52, 59, 54, 51, 56, 53, 55]

    1. Calculate the sample mean for Group A and Group B.
    2. Conduct an independent two-sample t-test (Welch's t-test, equal_var=False)
       to determine whether Group B exhibits a statistically significant improvement.
    3. Interpret the resulting t-statistic and p-value at alpha = 0.05.
================================================================================
"""

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

# ==============================================================================
# ASM PRACTICAL 6
# ==============================================================================
"""
================================================================================
PRACTICAL 6: LINEAR REGRESSION & CORRELATION
================================================================================
FULL QUESTIONS:

Question 1: (Simple Linear Regression)
    Load the scikit-learn Diabetes dataset into a pandas DataFrame.
    1. Evaluate the Pearson correlation between Body Mass Index ('bmi') and the
       disease progression outcome ('target').
    2. Fit an Ordinary Least Squares (OLS) Simple Linear Regression model
       (target ~ bmi + intercept) using statsmodels.
    3. Output and interpret the model summary (R-squared, coefficients, p-values).

Question 2: (Multiple Linear Regression)
    Fit an OLS Multiple Linear Regression model predicting disease progression ('target')
    using three predictors: 'bmi', blood pressure ('bp'), and 'age'.
    Add an intercept constant and evaluate:
    - Overall model fit (R-squared, F-statistic).
    - Which individual variables are statistically significant predictors.

Question 3: (Spearman Rank Correlation)
    Given:
    study_time = [2, 4, 1, 5, 3]
    exam_score = [50, 65, 45, 80, 60]
    Calculate the Spearman rank correlation coefficient and p-value.
    Interpret the monotonic relationship between study time and exam score.
================================================================================
"""

from sklearn.datasets import load_diabetes
import pandas as pd
import statsmodels.api as sm

diabetes = load_diabetes(as_frame=True)
df = diabetes.frame
print(df.head())

# correlation
print(df[["bmi", "target"]].corr())

# Simple linear regression
X = sm.add_constant(df["bmi"])
y = df['target']
model = sm.OLS(y, X).fit()
print(model.summary())

# Question 2: Multiple Linear Regression
X = df[["bmi", "bp", "age"]]
X = sm.add_constant(X)
model = sm.OLS(df["target"], X).fit()
print(model.summary())

# Question 3: Spearman Rank Correlation
from scipy.stats import spearmanr

study_time = [2, 4, 1, 5, 3]
exam_score = [50, 65, 45, 80, 60]

correlation, p_value = spearmanr(study_time, exam_score)
print("Spearman Correlation:", correlation)
print("P-value:", p_value)

# ==============================================================================
# ASM PRACTICAL 7
# ==============================================================================
"""
================================================================================
PRACTICAL 7: LOGISTIC REGRESSION & CLASSIFICATION
================================================================================
FULL QUESTIONS:

Question 1: (Customer Churn Prediction with Logistic Regression)
    Load the customer churn prediction dataset ('scikit-learn/churn-prediction').
    1. Use 'tenure' and 'MonthlyCharges' as predictors to predict binary 'Churn' (No=0, Yes=1).
    2. Split data into training (80%) and testing (20%) sets using stratified sampling.
    3. Fit a Logistic Regression model on the training set.
    4. Predict on the test set and evaluate using:
       - Confusion Matrix
       - Accuracy, Precision, Recall, F1-Score
       - Classification Report
    5. Compute predicted probabilities, generate the ROC curve, and calculate the AUC score.

Question 2: (Binary Classification Pipeline on Palmer Penguins)
    Load the Palmer Penguins dataset and filter for species 'Adelie' and 'Gentoo'.
    1. Use four features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g.
    2. Encode target species: Adelie=0, Gentoo=1.
    3. Build a Machine Learning Pipeline consisting of:
       - StandardScaler()
       - LogisticRegression(max_iter=1000)
    4. Train on 80% train split and evaluate on 20% test split.
    5. Output Confusion Matrix, Accuracy, Precision, Recall, F1-Score,
       Classification Report, and ROC Curve with AUC score.
================================================================================
"""

from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Load dataset
dataset = load_dataset("scikit-learn/churn-prediction")
df = dataset["train"].to_pandas()

# Select predictors and target
X = df[["tenure", "MonthlyCharges"]]
y = df["Churn"].map({"No": 0, "Yes": 1})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state = 42,
    stratify = y
)

# Fit logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Confusion Matrix
print("Confusion Matix:")
print(confusion_matrix(y_test,y_pred))

# Performance metrics
print("\nPerfomance Metrics")
print("---------------------")
print("Accuracy:", accuracy_score(y_test,y_pred))
print("Precision:", precision_score(y_test,y_pred))
print("Recall:", recall_score(y_test,y_pred))
print("F1-score:", f1_score(y_test,y_pred))

# Complete classification report
print("\nClassification Report:")
print(classification_report(y_test,y_pred))

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Predicted probabilities for churn
y_prob = model.predict_proba(X_test)[:,1]

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# AUC
auc = roc_auc_score(y_test, y_prob)
print("AUC:", auc)

# Plot ROC curve
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {auc:.3f})")
plt.plot([0, 1], [0,1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Customer Churn")
plt.legend()
plt.show()

# Question 2: Palmer Penguins Dataset (Adelie vs Gentoo)
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load dataset
dataset = sns.load_dataset("penguins")
df = dataset.copy()
df = dataset[dataset["species"].isin(["Adelie", "Gentoo"])].copy()

features = [
    "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"
]

df = df[features + ["species"]].dropna()

X = df[features]
y = (df["species"] == "Gentoo").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state=42,
    stratify=y
)

# Standardize and fit logistic regression
model = Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Confusion matrix
print(f"Confusion Matrix: \n{confusion_matrix(y_test, y_pred)}")

# Performance metrics
print(f"\nPerformance Metrics: \nAccuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")
print(f"F1 Score: {f1_score(y_test, y_pred)}")

# Classification report
print(f"\nClassification Report: \n{classification_report(y_test, y_pred)}\n")
print(f"\nInterpretation: \nThus, the model is correct 100% of times.")

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# AUC
auc = roc_auc_score(y_test, y_prob)
print("AUC: ", auc)

# Plot ROC curve
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc: .3f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Adelie/Gentoo")
plt.legend()
plt.show()

# ==============================================================================
# ASM PRACTICAL 8
# ==============================================================================
"""
================================================================================
PRACTICAL 8: PRINCIPAL COMPONENT ANALYSIS (PCA)
================================================================================
FULL QUESTIONS:

Question 1 & 2: (PCA on Wine Dataset)
    Load the scikit-learn Wine dataset (178 samples, 13 features).
    1. Standardize all 13 features using StandardScaler.
    2. Apply PCA and calculate the Explained Variance Ratio and Cumulative Explained Variance.
    3. Determine the minimum number of principal components required to retain
       at least 90% of the total variance.
    4. Transform the dataset using PCA with 2 components and plot a 2D scatter plot
       colored by wine class to visualize class separability.

Question 3: (PCA on Breast Cancer Dataset with Scree Plot)
    Load the scikit-learn Breast Cancer dataset (569 observations, 30 features).
    1. Standardize all 30 features using StandardScaler.
    2. Apply PCA and compute the cumulative explained variance.
    3. Find the minimum number of components explaining at least 90% variance.
    4. Plot the Cumulative Explained Variance curve (scree plot) with a red dashed
       line at 90% variance threshold.
================================================================================
"""

import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# loading dataset
wine = load_wine()
x = pd.DataFrame(data=wine.data, columns=wine.feature_names)
y = wine.target

print("Original dataset shape", x.shape)
print("First five observation\n", x.head())

# standardization
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# applying pca 
pca = PCA()
x_pca = pca.fit_transform(x_scaled)

# explained variance 
explained_variance = pca.explained_variance_ratio_
print("Explained variance ratio", explained_variance)

# cumulative explained variance
cumulative_variance = explained_variance.cumsum()
print("Cumulative explained variance", cumulative_variance)

# number of components explaining at least 90% 
n_components = (cumulative_variance >= 0.9).argmax() + 1
print("Number of components explaining at least 90% variance", n_components)

# Transform using selected components
pca_reduced = PCA(n_components=n_components)
x_reduced = pca_reduced.fit_transform(x_scaled)

# reduced dataset shape
print("Reduced dataset shape", x_reduced.shape)

# Q2: PCA with two components visualization
pca_2 = PCA(n_components=2)
x_pca_2 = pca_2.fit_transform(x_scaled)
print(x_pca_2.shape)

plt.figure(figsize=(8,6))
plt.scatter(x_pca_2[:,0], x_pca_2[:,1], c=y)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA of Wine Dataset')
plt.colorbar(label="Wine Class")
plt.show()

# Q3: Cancer Dataset PCA
from sklearn.datasets import load_breast_cancer
import numpy as np

cancer = load_breast_cancer()
x = cancer.data
y = cancer.target
target_names = cancer.target_names
feature_names = cancer.feature_names

print("Number of observations", x.shape[0])
print("Number of features", x.shape[1])
print("Target Name:\n", target_names)

# Standardization
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Applying PCA
pca = PCA()
x_pca = pca.fit_transform(x_scaled)

# Explained variance ratio
explained_variance = pca.explained_variance_ratio_
print("Explained variance ratio:\n", explained_variance)

# Cumulative explained variance
cumulative_variance = explained_variance.cumsum()
print("Cumulative explained variance:\n", cumulative_variance)

# Number of components explaining at least 90% variance
n_components = np.argmax(cumulative_variance >= 0.90) + 1
print("Number of components explaining at least 90% variance:", n_components)

# Transform using selected components
pca_reduced = PCA(n_components=n_components)
x_reduced = pca_reduced.fit_transform(x_scaled)

# Reduced dataset shape
print("Reduced dataset shape:", x_reduced.shape)

# Plot cumulative explained variance
plt.plot(
    range(1, len(cumulative_variance) + 1),
    cumulative_variance,
    marker='o'
)
plt.axhline(y=0.90, color='red', linestyle='--', label='90% variance')
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA - Cancer Dataset")
plt.legend()
plt.grid(True)
plt.show()

# ==============================================================================
# ASM PRACTICAL 9
# ==============================================================================
"""
================================================================================
PRACTICAL 9: BAYESIAN UPDATING FOR MEDICAL DIAGNOSTIC TESTING
================================================================================
FULL QUESTIONS:

Question: (Bayes' Theorem in Medical Diagnostic Testing)
    A diagnostic test for a disease has the following epidemiological characteristics:
    - Prior probability of disease in the population: P(Disease) = 0.01 (1%)
    - Test Sensitivity (True Positive Rate): P(+ | Disease) = 0.95 (95%)
    - Test Specificity (True Negative Rate): P(- | No Disease) = 0.90 (90%)
    - False Positive Rate: P(+ | No Disease) = 1 - Specificity = 0.10 (10%)

    Using Bayes' Theorem:
    1. Calculate the total probability of a positive test:
       P(+) = P(+ | Disease) * P(Disease) + P(+ | No Disease) * P(No Disease)
    2. Calculate the posterior probability of disease given a positive test:
       P(Disease | +) = [P(+ | Disease) * P(Disease)] / P(+)
    3. Interpret the result in terms of the Base-Rate Fallacy.
================================================================================
"""

prior_disease = 0.01

# Test characteristics
sensitivity = 0.95
specificity = 0.90

# Probability of a positive test among people without disease
false_positive_rate = 1 - specificity

# Bayes' theorem after first positive test
prob_positive = (
    sensitivity * prior_disease +
    false_positive_rate * (1 - prior_disease)
)

# Posterior probability P(Disease | Positive)
posterior_disease = (sensitivity * prior_disease) / prob_positive

print("Prior Probability of Disease:", prior_disease)
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)
print("False Positive Rate:", false_positive_rate)
print("Probability of Positive Test:", prob_positive)
print("Posterior Probability of Disease given Positive Test:", posterior_disease)