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
