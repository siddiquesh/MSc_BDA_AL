"""
================================================================================
APPLIED STATISTICAL METHODS (ASM) - PRACTICALS 1 TO 9
MSc Big Data Analytics
================================================================================
"""

# ==============================================================================
# ASM PRACTICAL 1: Descriptive Statistics (Iris, Tips, Stock Market)
# ==============================================================================
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt

# Q1) Iris Dataset
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

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 2, i + 1)
    sns.histplot(iris[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel('col')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Q2) Tips Dataset
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

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(2, 2, i + 1)
    sns.histplot(tips[col], kde=True, bins=15)
    plt.title(f'Distribution of {col}')
    plt.xlabel('col')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Q3) Stock Dataset
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
# ASM PRACTICAL 2: Probability Distributions (Normal, Binomial, Poisson)
# ==============================================================================
from scipy import stats

# Q1) Normal Distribution
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

# Q2) Effect of Standard Deviation
mu = 70
x = np.linspace(20, 120, 500)
pdf1 = stats.norm.pdf(x, loc=mu, scale=5)
pdf2 = stats.norm.pdf(x, loc=mu, scale=10)
pdf3 = stats.norm.pdf(x, loc=mu, scale=15)
plt.figure(figsize=(9, 5))
plt.plot(x, pdf1, label="sigma = 5")
plt.plot(x, pdf2, label="sigma = 10")
plt.plot(x, pdf3, label="sigma = 15")
plt.xlabel("Marks")
plt.ylabel("Probability Density Function")
plt.title("Effect of Standard Deviation and Normal Distribution")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Q3) Effect of Mean
sigma = 10
x = np.linspace(20, 120, 500)
pdf1 = stats.norm.pdf(x, loc=50, scale=sigma)
pdf2 = stats.norm.pdf(x, loc=70, scale=sigma)
pdf3 = stats.norm.pdf(x, loc=90, scale=sigma)
plt.figure(figsize=(9, 5))
plt.plot(x, pdf1, label="mean = 50")
plt.plot(x, pdf2, label="mean = 70")
plt.plot(x, pdf3, label="mean = 90")
plt.xlabel("Marks")
plt.ylabel("Probability Density Function")
plt.title("Effect of Mean and Normal Distribution")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Q4) Binomial Distribution
n = 20
p = 0.3
x = np.arange(0, n + 1)
pmf = stats.binom.pmf(x, n, p)
plt.stem(x, pmf)
plt.xlabel("Number of Purchases")
plt.ylabel("Probability")
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
# ASM PRACTICAL 3: Confidence Intervals & Bootstrapping
# ==============================================================================
delivery_time = np.array([
    31, 28, 35, 42, 30,
    27, 39, 33, 26, 32,
    34, 31, 38, 26, 32,
    41, 30, 36, 29, 37
])

n = len(delivery_time)
sample_mean = np.mean(delivery_time)
sample_sd = np.std(delivery_time, ddof=1)
df_deg = n - 1
SE = sample_sd / np.sqrt(n)

t_critical = stats.t.ppf(0.975, df_deg)
margin_error = t_critical * SE
lower = sample_mean - margin_error
upper = sample_mean + margin_error

print("Sample Mean =", sample_mean)
print("Sample SD =", sample_sd)
print("Degrees of Freedom =", df_deg)
print("Standard Error =", SE)
print("Margin of Error =", margin_error)
print("95% Confidence Interval =", (lower, upper))

# Bootstrap CI
np.random.seed(42)
bootstrap_means = []
for i in range(5000):
    bootstrap_sample = np.random.choice(
        delivery_time, size=len(delivery_time), replace=True
    )
    bootstrap_means.append(np.mean(bootstrap_sample))

bootstrap_means = np.array(bootstrap_means)
lower_bootstrap = np.percentile(bootstrap_means, 2.5)
upper_bootstrap = np.percentile(bootstrap_means, 97.5)

print("Bootstrap Mean =", np.mean(bootstrap_means))
print("95% Bootstrap CI =", (lower_bootstrap, upper_bootstrap))
print("t-based CI =", (lower, upper))
print("Bootstrap CI =", (lower_bootstrap, upper_bootstrap))
print("t-based CI width =", lower - upper)
print("Bootstrap CI width =", upper_bootstrap - lower_bootstrap)


# ==============================================================================
# ASM PRACTICAL 4: Hypothesis Testing (t-test, Chi-square, ANOVA, Tukey HSD)
# ==============================================================================
from scipy.stats import chi2_contingency, f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Q1: Two-sample t-test
df_titanic = sns.load_dataset("titanic")
male = df_titanic[df_titanic["sex"] == "male"]["fare"].dropna()
female = df_titanic[df_titanic["sex"] == "female"]["fare"].dropna()

t_stat, p_value = stats.ttest_ind(male, female, equal_var=False)
print("t_statistic:", t_stat)
print("p-value:", p_value)

# Q2: Chi-square test
table = pd.crosstab(df_titanic["class"], df_titanic["survived"])
print(table)
chi2, p_val, dof, expected = chi2_contingency(table)
print("Chi-square statistics:", chi2)
print("Degrees of Freedom:", dof)
print("p-value:", p_val)

# Q3: ANOVA & Tukey HSD
first = df_titanic[df_titanic["class"] == "First"]["fare"].dropna()
second = df_titanic[df_titanic["class"] == "Second"]["fare"].dropna()
third = df_titanic[df_titanic["class"] == "Third"]["fare"].dropna()

F, p_val_anova = f_oneway(first, second, third)
print("F-statistic:", F)
print("p-value:", p_val_anova)

df_clean = df_titanic.dropna(subset=["fare"])
tukey = pairwise_tukeyhsd(endog=df_clean["fare"], groups=df_clean["class"])
print(tukey)


# ==============================================================================
# ASM PRACTICAL 5: A/B Testing
# ==============================================================================
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
t_stat, p_val = ttest_ind(group_A, group_B, equal_var=False)

print("Mean - Group A:", mean_A)
print("Mean - Group B:", mean_B)
print("t-statistic:", t_stat)
print("p-value:", p_val)


# ==============================================================================
# ASM PRACTICAL 6: Linear Regression & Spearman Correlation
# ==============================================================================
from sklearn.datasets import load_diabetes
import statsmodels.api as sm
from scipy.stats import spearmanr

# Q1: Simple Linear Regression
diabetes = load_diabetes(as_frame=True)
df_diab = diabetes.frame
print(df_diab.head())
print(df_diab[["bmi", "target"]].corr())

X = sm.add_constant(df_diab["bmi"])
y = df_diab['target']
model = sm.OLS(y, X).fit()
print(model.summary())

# Q2: Multiple Linear Regression
X_multi = df_diab[["bmi", "bp", "age"]]
X_multi = sm.add_constant(X_multi)
model_multi = sm.OLS(df_diab["target"], X_multi).fit()
print(model_multi.summary())

# Q3: Spearman Rank Correlation
study_time = [2, 4, 1, 5, 3]
exam_score = [50, 65, 45, 80, 60]
corr, p_v = spearmanr(study_time, exam_score)
print("Spearman Correlation:", corr)
print("P-value:", p_v)


# ==============================================================================
# ASM PRACTICAL 7: Logistic Regression & Classification
# ==============================================================================
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, roc_auc_score
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Q1: Churn Prediction
dataset = load_dataset("scikit-learn/churn-prediction")
df_churn = dataset["train"].to_pandas()

X = df_churn[["tenure", "MonthlyCharges"]]
y = df_churn["Churn"].map({"No": 0, "Yes": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model_logit = LogisticRegression()
model_logit.fit(X_train, y_train)
y_pred = model_logit.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-score:", f1_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

y_prob = model_logit.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)
print("AUC:", auc)

plt.plot(fpr, tpr, label=f"ROC curve (AUC = {auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Customer Churn")
plt.legend()
plt.show()

# Q2: Palmer Penguins
penguins = sns.load_dataset("penguins")
df_peng = penguins[penguins["species"].isin(["Adelie", "Gentoo"])].copy()
features = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
df_peng = df_peng[features + ["species"]].dropna()

X = df_peng[features]
y = (df_peng["species"] == "Gentoo").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression(max_iter=1000))
])
model_pipe.fit(X_train, y_train)
y_pred = model_pipe.predict(X_test)
y_prob = model_pipe.predict_proba(X_test)[:, 1]

print(f"Confusion Matrix: \n{confusion_matrix(y_test, y_pred)}")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report: \n{classification_report(y_test, y_pred)}")


# ==============================================================================
# ASM PRACTICAL 8: Principal Component Analysis (PCA)
# ==============================================================================
from sklearn.datasets import load_wine, load_breast_cancer
from sklearn.decomposition import PCA

# Q1 & Q2: Wine Dataset
wine = load_wine()
x_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
y_wine = wine.target

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_wine)

pca = PCA()
x_pca = pca.fit_transform(x_scaled)
explained_var = pca.explained_variance_ratio_
cum_var = explained_var.cumsum()
n_comp = (cum_var >= 0.9).argmax() + 1
print("Number of components explaining at least 90% variance:", n_comp)

pca_2 = PCA(n_components=2)
x_pca_2 = pca_2.fit_transform(x_scaled)
plt.figure(figsize=(8, 6))
plt.scatter(x_pca_2[:, 0], x_pca_2[:, 1], c=y_wine)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA of Wine Dataset')
plt.colorbar(label="Wine Class")
plt.show()

# Q3: Cancer Dataset
cancer = load_breast_cancer()
x_cancer = cancer.data
y_cancer = cancer.target

scaler_c = StandardScaler()
x_cancer_scaled = scaler_c.fit_transform(x_cancer)
pca_c = PCA()
x_cancer_pca = pca_c.fit_transform(x_cancer_scaled)
cum_var_c = pca_c.explained_variance_ratio_.cumsum()
n_comp_c = np.argmax(cum_var_c >= 0.90) + 1
print("Cancer dataset components for 90% variance:", n_comp_c)


# ==============================================================================
# ASM PRACTICAL 9: Bayesian Updating for Medical Testing
# ==============================================================================
prior_disease = 0.01
sensitivity = 0.95
specificity = 0.90
false_positive_rate = 1 - specificity

prob_positive = (
    sensitivity * prior_disease +
    false_positive_rate * (1 - prior_disease)
)
posterior_disease = (sensitivity * prior_disease) / prob_positive

print("Prior Probability of Disease:", prior_disease)
print("Probability of Positive Test:", prob_positive)
print("Posterior Probability P(Disease | Positive):", posterior_disease)
