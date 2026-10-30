"""
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
print("\nExplained Variance Ratio:\n", explained_variance)

# Cumulative Explained Variance
cumulative_variance = explained_variance.cumsum()
print("\nCumulative Explained Variance:\n", cumulative_variance)

# Number of components explaining at least 90%
n_components = (cumulative_variance >= 0.9).argmax() + 1
print("\nNumber of components explaining at least 90% of variance:", n_components)

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
print("\n--- Q2: Breast Cancer Dataset PCA ---")
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
print("\nExplained Variance Ratio:\n", exp_var_c)

# Cumulative Explained Variance
cum_var_c = exp_var_c.cumsum()
print("\nCumulative Explained Variance:\n", cum_var_c)

# Number of components explaining at least 90%
n_comp_c = (cum_var_c >= 0.9).argmax() + 1
print("\nNumber of components explaining at least 90% of variance:", n_comp_c)

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