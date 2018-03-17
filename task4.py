from scipy import linalg
import numpy as np
import time
n=int(input('Matrix size'))

A=np.random.random((n,n))
k=np.arange(n)
for t in np.linspace(0.,10.,100):
    b=k/(1.+k*t)
    r1=linalg.solve(A,b)
print(r1)


lu,piv = linalg.lu_factor(A)
for t in np.linspace(0.,10.,100):
    b=k/(1.+k*t)
    r2=linalg.lu_solve((lu,piv), b)
print(r2)
Ainv=linalg.inv(A)
for t in np.linspace(0.,10.,100):
    b=k/(1.+k*t)
r3=np.dot(Ainv, b)
print(r3)

start_time=time.time()
for i in range (10000):
    linalg.solve(A,b)
print('time linalg.solve', time.time()-start_time)
start_time=time.time()
for i in range (10000):
    linalg.lu_solve((lu,piv), b)
print('time lu_solve', time.time()-start_time)
start_time=time.time()
for i in range (10000):
    np.dot(Ainv, b)
print('time inv', time.time()-start_time)

