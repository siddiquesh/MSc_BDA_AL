# =====================================================================
# PRACTICAL 1: Matrix Operations & Image Processing
# =====================================================================
import numpy as np

#create a 1-D array and dimension
v1=np.array([5,4,7,8])
print(v1)
print(v1.ndim)

#create a 2-D array
v2=np.array([[1,5,3],[4,7,9],[4,9,4]])
print(v2)

#create a matrix of 2 rows 3 column
v3=np.array([[1,5],[4,7],[4,9]])
print(v3)

#matrix addition
v4=np.array([[6,3,8],[2,5,2],[8,1,3]])
print(v4)
print('addition of v2 and v4 is \n',v2+v4)

#matrix subtraction
print('subtraction of v2 and v4 is \n',v2-v4)

# scalar matrix
print('scalar matrix of v4 is \n',2*v4)

# multiplication matrix
print(np.dot(v2,v4))
#element wise multiplication just use '*' for multiply.

#transpose of the matrix
print('transpose of matrix v2 is \n',v2.T)

#matrix determinant
a=np.array([[1,2,3],[1,1,5],[2,4,7]])
print('Matrix a= \n',a)
print('determinant of the a is',np.linalg.det(a))

#inverse of the matrix
print('inverse of the a is \n',np.linalg.inv(a))

b= np.array([[1,2,3],
             [1,1,5],
             [2,4,6]])

if np.linalg.det(b) != 0:
    print('inverse of a is \n',np.linalg.inv(b))
else:
    print('inverse does not exist for matrix having deteminant zero ')

# identity matrix 
print('identity matrix \n',np.eye(3)) #parameter is used to define the dimension of matrix

import matplotlib.pyplot as plt
from skimage import color,io
from skimage.transform import resize

image=io.imread('C:/Users/USER-11/Downloads/images.jpg')
#print(image)
gray_image=color.rgb2gray(image)
gray_image=resize(gray_image,(256,256))

#brighting the image
bright_image=gray_image*2.0
bright_image=np.clip(bright_image,0,1)

#noisy or distortion will be present in the image
noisy_image=gray_image+0.3
noisy_image=np.clip(noisy_image,0,1)

#darkening the image
dark_image=gray_image-0.2
dark_image=np.clip(dark_image,0,1)

#fliping the image
transpose_image=gray_image.T

#inversing the image
inverse_image=np.linalg.inv(gray_image)
inverse_image=np.clip(inverse_image,0,1)

#plotting the original image
plt.imshow(image, cmap='gray')
plt.title('original image')
plt.show()

plt.figure(figsize=(12,12))
plt.subplot(2,3,1)
plt.imshow(gray_image,cmap='gray')
plt.title('Original Gray Image')

plt.figure(figsize=(12,12))
plt.subplot(2,3,2)
plt.imshow(bright_image,cmap='gray')
plt.title('Bright Image')

plt.figure(figsize=(12,12))
plt.subplot(2,3,3)
plt.imshow(noisy_image,cmap='gray')
plt.title('noisy Image')

plt.figure(figsize=(12,12))
plt.subplot(2,3,4)
plt.imshow(dark_image,cmap='gray')
plt.title('dark Image')

plt.figure(figsize=(12,12))
plt.subplot(2,3,5)
plt.imshow(transpose_image,cmap='gray')
plt.title('transpose Image')

plt.figure(figsize=(12,12))
plt.subplot(2,3,6)
plt.imshow(inverse_image,cmap='gray')
plt.title('inverse Image')


# =====================================================================
# PRACTICAL 2A: Gaussian Elimination
# =====================================================================
import numpy as np
'''
system of equation
2x+y-z=8
-3x-y+2z=-11
-2x+y+2z=-3
'''
A=np.array([[2,1,-1],[-3,-1,2],[-2,1,2]],dtype=float)
B=np.array([8.0,-11.0,-3.0])

print('co-efficient matrix A:\n',A)
print('Right hand side matrix B:\n',B)

def gaussian_elimination(A,B):
    n=len(B)
    # forward elimination
    for i in range(n):
        for j in range(i+1,n):
            ratio =A[j][i]/A[i][i]
            A[j,i:]=A[j,i:]-ratio*A[i,i:]
            B[j]=B[j]-ratio*B[i]
    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        x[i]=(B[i]-np.dot(A[i,i+1:],x[i+1:]))/A[i][i]
    return x

gauss=gaussian_elimination(A,B)
print(A)
print('Solution by gaussian elimination :\n',gauss)

C=np.array([[1,1,2],[2,3,6],[3,6,10]],dtype=float)
D=np.array([4.0,10.0,17.0])

def gaussian_eliminate(C,D):
    n=len(B)
    # forward elimination
    for i in range(n):
        for j in range(i+1,n):
            ratio =C[j][i]/C[i][i]
            C[j,i:]=C[j,i:]-ratio*C[i,i:]
            D[j]=D[j]-ratio*D[i]
    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        x[i]=(D[i]-np.dot(C[i,i+1:],x[i+1:]))/C[i][i]
    return x

gaus=gaussian_eliminate(C,D)
print(C)
print('Solution by gaussian elimination :\n',gaus)


# =====================================================================
# PRACTICAL 2B: LU Factorization
# =====================================================================
import numpy as np
from scipy.linalg import lu,lu_factor, lu_solve
A=np.array(([3,-1,2],[-3,-2,10],[9,-5,6]), dtype=float)
b=np.array([10,20,30],dtype=float)
P,L,U=lu(A)
print("Matrix A: \n",A)
print("Matrix Permutation: \n",P)
print("Matrix Lower: \n",L)
print("Matrix Upper: \n",U)
lu_factorization = lu_factor(A)
print("LU Factorization: \n",lu_factorization)
x=lu_solve(lu_factorization,b)
print("Solution: \n",x)

#
import numpy as np
from scipy.linalg import lu,lu_factor, lu_solve
A=np.array(([3,-1],[4,1]), dtype=float)
b=np.array([1,6],dtype=float)
P,L,U=lu(A)
print("Matrix A: \n",A)
print("Matrix Permutation: \n",P)
print("Matrix Lower: \n",L)
print("Matrix Upper: \n",U)
lu_factorization = lu_factor(A)
print("LU Factorization: \n",lu_factorization)
x=lu_solve(lu_factorization,b)
print("Solution: \n",x)

#user input equation
a1,b1,c1,d1=map(float,input("Enter the equation 1 (a1,b1,c1,d1):").split())
a2,b2,c2,d2=map(float,input("Enter the equation 2 (a2,b2,c2,d2):").split())
a3,b3,c3,d3=map(float,input("Enter the equation 3 (a3,b3,c3,d3):").split())
A=np.array(([a1,b1,c1],[a2,b2,c2],[a3,b3,c3]), dtype=float)
b=np.array([d1,d2,d3],dtype=float)
P,L,U=lu(A)
print("Matrix A: \n",A)
print("Matrix Permutation: \n",P)
print("Matrix Lower: \n",L)
print("Matrix Upper: \n",U)
lu_factorization = lu_factor(A)
print("LU Factorization: \n",lu_factorization)
x=lu_solve(lu_factorization,b)
print("Solution: \n",x)

import pandas as pd
# Load the file from Colab's default storage path
df= pd.read_csv('/content/book_sale.csv')
# View the first 5 rows
print(df.head())
A=df.iloc[:,0:3].to_numpy()
b=df.iloc[:,3].to_numpy()
print('matrix A\n',A)
print('vector b\n',b)


# =====================================================================
# PRACTICAL 3: Simple Linear Regression
# =====================================================================
# linear regression using formula
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,4,5,4,5])

X_mean = np.mean(x)
Y_mean = np.mean(y)

numerator= np.sum((x - X_mean)* (y - Y_mean))
denominator = np.sum((x - X_mean) ** 2)
slope = numerator / denominator
intercept = Y_mean - slope * X_mean

print("Slope: ", slope)
print("Intercept: ", intercept)

y_pred = slope * x + intercept
print(y_pred)

plt.scatter(x,y, color="black", label="Actual Data")
plt.plot(x,y_pred, color='red', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

# Linear Regression using pre build function
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#-1 (Rows): Tells NumPy to automatically calculate the number of rows. 
# Since there are 5 elements total, NumPy computes (5 / 1 = 5) rows.
x=np.array([1,2,3,4,5]).reshape(-1,1) 
y=np.array([2,4,5,4,5])

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *
import pandas as pd

housing = pd.read_csv('Housing.csv')

#Select feature and Target
x= housing[["area"]]
y = housing['price']

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

print("R2 Score: ",r2_score(y,model.predict(x)))
print("MSE: ",mean_squared_error(y,model.predict(x)))

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

#Select feature and Target on bedroom
x= housing[["bedrooms"]]
y = housing['price']

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

print("R2 Score: ",r2_score(y,model.predict(x)))
print("MSE: ",mean_squared_error(y,model.predict(x)))

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *

x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([2,4,6,8,9])

model=LinearRegression()
model.fit(x,y)

print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

y_pred=model.predict(x)

print("R2 Score: ",r2_score(y,model.predict(x)))
print("MSE: ",mean_squared_error(y,model.predict(x)))

plt.scatter(x,y, color="blue", label="Actual Data")
plt.plot(x,y_pred, color='green', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()


# =====================================================================
# PRACTICAL 4: Principal Component Analysis (PCA)
# =====================================================================
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


# =====================================================================
# PRACTICAL 5: SVD Image Compression
# =====================================================================
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.metrics import mean_squared_error

#step 1: Load image and convert to grayscale
img = io.imread('images.jpg')
gray = color.rgb2gray(img) # values between 0-1

plt.imshow(gray, cmap='gray')
plt.title("Original GrayScale Image")
plt.axis('off')
plt.show()

# step 2: Apply SVD
U, S , Vt = np.linalg.svd(gray, full_matrices=False)
# returns U and Vt with shapes (m,k) and (k,n) instead of full sq sizes(m,m) and

#step 3 : Function to reconstruct with top r values
def reconstruct(U, S, Vt, r):
    return U[:, :r] @ np.diag(S[:r]) @ Vt[:r, :]

#step 4: Choose r values
r1,r2,r3,r4,r5,r6,r7,r8,r9 = 5,20,50,100,150,200,500,800,1100

#Step 5 : Reconstruct images
img_r1 = reconstruct(U, S, Vt, r1)
img_r2 = reconstruct(U, S, Vt, r2)
img_r3 = reconstruct(U, S, Vt, r3)
img_r4 = reconstruct(U, S, Vt, r4)
img_r5 = reconstruct(U, S, Vt, r5)
img_r6 = reconstruct(U, S, Vt, r6)
img_r7 = reconstruct(U, S, Vt, r7)
img_r8 = reconstruct(U, S, Vt, r8)
img_r9 = reconstruct(U, S, Vt, r9)

plt.close('all')
plt.figure(figsize=(18, 12))

plt.subplot(3, 3, 1)
plt.imshow(img_r1, cmap='gray')
plt.title(f"r={r1}")
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(img_r2, cmap='gray')
plt.title(f"r={r2}")
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(img_r3, cmap='gray')
plt.title(f"r={r3}")
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(img_r4, cmap='gray')
plt.title(f"r={r4}")
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(img_r5, cmap='gray')
plt.title(f"r={r5}")
plt.axis('off')

plt.subplot(3, 3, 6)
plt.imshow(img_r6, cmap='gray')
plt.title(f"r={r6}")
plt.axis('off')

plt.subplot(3, 3, 7)
plt.imshow(img_r7, cmap='gray')
plt.title(f"r={r7}")
plt.axis('off')

plt.subplot(3, 3, 8)
plt.imshow(img_r8, cmap='gray')
plt.title(f"r={r8}")
plt.axis('off')

plt.subplot(3, 3, 9)
plt.imshow(img_r9, cmap='gray')
plt.title(f"r={r9}")
plt.axis('off')

plt.tight_layout()
plt.show()

#Step 6: Compute mse
mse_r1 = mean_squared_error(gray, img_r1)
mse_r2 = mean_squared_error(gray, img_r2)
mse_r3 = mean_squared_error(gray, img_r3)
mse_r4 = mean_squared_error(gray, img_r4)
mse_r5 = mean_squared_error(gray, img_r5)
mse_r6 = mean_squared_error(gray, img_r6)
mse_r7 = mean_squared_error(gray, img_r7)
mse_r8 = mean_squared_error(gray, img_r8)
mse_r9 = mean_squared_error(gray, img_r9)

print(mse_r1)
print(mse_r2)
print(mse_r3)
print(mse_r4)
print(mse_r5)
print(mse_r6)
print(mse_r7)
print(mse_r8)
print(mse_r9)


# =====================================================================
# PRACTICAL 6: K-Means Clustering with Distance Metrics
# =====================================================================
import numpy as np

#Euclidean Distance
def euclidean_distance(a,b):
    return np.sqrt(np.sum((a-b)**2))

#Manhattan Distance
def manhattan_distance(a,b):
    return np.sum(np.abs(a-b))

def kmeans_custom(X, max_iters=10):
    centroids = np.array([[1,0,0],[0,1,1]]) #2 centroids
    for i in range (max_iters):
        clusters = [[] for i in range(2)]
        
        #Assign points to clusters
        for point in X:
            distances = []
            for centroid in centroids:
                distances.append(manhattan_distance(point, centroid))
            
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)
        
        # Update Centroid
        new_centroids = []
        for cluster in clusters:
            new_centroids.append(np.mean(cluster, axis=0))
        
        new_centroids = np.array(new_centroids)
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return np.array(centroids), clusters

x = np.array([[1,2,3,],[0,1,2],[3,0,5],[4,1,3],[5,0,1]])
print(x)

centroids_x, clusters_x = kmeans_custom(x)
print("Centroids of X: \n", centroids_x)
print("Clusters of X: \n", clusters_x)

import matplotlib.pyplot as plt
def plot_clusters_2D(x,clusters,centroid):
    colors=['r','g']
    plt.figure(figsize=(10,6))
    for i, cluster in enumerate(clusters):
        cluster = np.array(cluster)
        plt.scatter(cluster[:,0], cluster[:,1], color = colors[i])
    plt.scatter(centroid[:,0],centroid[:,1], c="black", marker="x", s = 300)
    plt.title("Manhattan Distance")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

centroids_x, clusters_x = kmeans_custom(x) #Function call
plot_clusters_2D(x, clusters_x, centroids_x)
