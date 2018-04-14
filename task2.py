import numpy as np
import math
# define a custom-build root-finding function (e.g. the one discussed in Lecture 1)
def f(x):
    return np.cos(x)/(x*x+1.)
a=0.1
b=2.4

x=np.linspace(0.,5.,100)
def fprime(x):
    return -(np.sin(x)*(x*x+1)+np.cos(x)*2*x)/((x*x+1)**2)
import scipy
from scipy import optimize
x_bisect = optimize.bisect (f,a,b)
x_newton = optimize.newton (f,(a+b)/2.,fprime)
x_brentq = optimize.brentq (f,a,b)
x_seq = optimize.newton (f,(a+b)/2.)
import time
start_time=time.time()
for i in range (10000):
    optimize.bisect(f,a,b)
print('time bisect ', time.time()-start_time)
start_time=time.time()
for i in range (10000):
    optimize.newton(f,(a+b)/2,fprime)
print('time newton ', time.time()-start_time)
start_time=time.time()
for i in range (10000):
    optimize.brentq(f,a,b)
print('time brentq', time.time()-start_time)
start_time=time.time()
for i in range (10000):
    optimize.newton(f,a)
print('time secant', time.time()-start_time)
print('bisect = ', x_bisect, 'newton = ', x_newton, 'brentq = ', x_brentq, 'secant = ', x_seq)

