import numpy as np
from scipy import linalg

n=int(input('Enter number of equations '))
A=np.zeros((n,n))
i,j=np.indices((n,n))
A[i==j]=1
A[i==j+1]=1
A[i==j+2]=1
B=np.arange(n)
x=linalg.solve(A,B)
print(x)
#Check that the solution is correct:


