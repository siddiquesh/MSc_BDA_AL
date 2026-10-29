import numpy as np
np.random.seed(42)
x=np.random.rand(100,2) @ np.array([[2,1],[1,3]]) # @ sign is used for multiplication
print(x)

# step 2 : Standardize
x_mean = x - np.mean(x,axis=0)

# step 3 : Covariance matrix
cov_matrix = np.cov(x_mean, rowvar=False)
print("Covariance matrix: ",cov_matrix)

# STEP 4 : Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
print("Eigenvalues: ",eigenvalues)
print("Eigenvectors: ",eigenvectors)

#STEP 5 : sort eigenvectors by eigenvalues (descending)
sorted_idx = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[sorted_idx]
eigenvectors = eigenvectors[:,sorted_idx]
print("Eigenvalues: ",eigenvalues)
print("Eigenvectors: ",eigenvectors)

#step 6 : project data onto first principal component (reduce to 1D)
pc1=eigenvectors[:,0]
print("pc1 \n",pc1)

x_pca=x_mean @pc1
print("x pca\n",x_pca) #projected on pc1

import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data

# step 2 : Standardize
x_mean = x - np.mean(x,axis=0)

# step 3 : Covariance matrix
cov_matrix = np.cov(x_mean, rowvar=False)

# STEP 4 : Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

#STEP 5 : sort eigenvectors by eigenvalues (descending)
sorted_idx = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[sorted_idx]
eigenvectors = eigenvectors[:,sorted_idx]

#step 6 : project data onto first principal component (reduce to 1D)
pc1=eigenvectors[:,:2]

x_pca=x_mean @pc1

print("Eigenvalues: ",eigenvalues)
print("Principal components: ",eigenvectors)
print("x pca\n",x_pca) #projected on pc1
