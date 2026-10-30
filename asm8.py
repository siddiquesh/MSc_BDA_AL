"""
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
print("First five observations:
", x.head())

# Standardization
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Applying PCA
pca = PCA()
x_pca = pca.fit_transform(x_scaled)

# Explained variance
explained_variance = pca.explained_variance_ratio_
print("
Explained variance ratio:
", explained_variance)

# Cumulative explained variance
cumulative_variance = explained_variance.cumsum()
print("
Cumulative explained variance:
", cumulative_variance)

# Number of components explaining at least 90%
n_components = (cumulative_variance >= 0.9).argmax() + 1
print("
Number of components explaining at least 90% variance:", n_components)

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

print("
" + "="*50)
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
print("
Explained variance ratio:
", explained_variance)

# Cumulative explained variance
cumulative_variance = explained_variance.cumsum()
print("
Cumulative explained variance:
", cumulative_variance)

# Number of components explaining at least 90%
n_components = (cumulative_variance >= 0.9).argmax() + 1
print("
Number of components explaining at least 90% variance:", n_components)

# Transform using selected components
pca_reduced = PCA(n_components=n_components)
x_reduced = pca_reduced.fit_transform(x_scaled)
print("Reduced dataset shape:", x_reduced.shape)
