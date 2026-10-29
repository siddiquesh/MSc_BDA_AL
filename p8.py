# ASM Practical 8 - Principal Component Analysis (PCA)

# Q1: Wine Dataset PCA
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
