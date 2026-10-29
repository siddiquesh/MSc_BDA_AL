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
