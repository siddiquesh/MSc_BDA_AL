# ASM Practical 4 - Hypothesis Testing (t-test, Chi-square, ANOVA, Tukey HSD)

# Question 1: Two-Sample t-test
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
