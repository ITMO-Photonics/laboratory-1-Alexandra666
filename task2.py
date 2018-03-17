import numpy as np
import math
# define a custom-build root-finding function (e.g. the one discussed in Lecture 1)
def f(x):
    return math.cos(x)/(x*x+1.)
a=0.1
b=2.4
tolerance=1.e-3

if( f(a)*f(b)>0. ):
    print('Error: f(a) and f(b) should have opposite signs! Stopping.')
else:
    while(0.5*(b-a) > tolerance):
        c = 0.5*(a+b)
        if( f(a)*f(c)<0. ):
            b=c
        else:
            a=c    
    print('result: ',0.5*(b+a))

x=np.linspace(0.,5.,100)

import scipy
from scipy import optimize
x_bisect = optimize.bisect (f,a,b)
x_newton = optimize.newton (f,a)
x_brentq = optimize.brentq (f,a,b)
import time
start_time=time.time()
for i in range (10000):
    optimize.bisect(f,a,b)
print('time bisect ', time.time()-start_time)
for i in range (10000):
    optimize.newton(f,a)
print('time newton ', time.time()-start_time)
for i in range (10000):
    optimize.bisect(f,a,b)
print('time brentq', time.time()-start_time)
print('bisect = ', x_bisect, 'newton = ', x_newton, 'brentq = ', x_brentq,)

