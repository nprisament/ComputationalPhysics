# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:01:16 2019

@author: npris
"""

import numpy as np
import matplotlib.pyplot as plt

tolerance = 0.5 * 10**-6

def bisect(f,a,b):
    c = []
    while (abs(b - a) / 2 > tolerance):
        c.append((a + b) / 2)
        if (f(c[-1]) == 0):
            return c
        if f(c[-1]) * f(a) < 0:
            b = c[-1]
        else:
            a = c[-1]
    c.append((a + b) / 2)
    return c

def newton(f,df,x0):
    x = [x0]
    while True:
        x.append(x[-1] - f(x[-1]) / df(x[-1]))
        if (abs(x[-1] - x[-2]) < tolerance):
            break
    return x

def find_multiple_zeros_bisect(f,a,b):
    ans = []
    a0 = b0 = a
    for i in np.arange(a,b,0.1):
        if (f(a0) * f(b0) < 0):
            x = bisect(f,a0,b0)
            if x[-1] not in ans:
                ans.append(x[-1])    
            a0 = b0
        else:
            b0 = i
        if (f(a0) == 0):
            a0 = i
    return ans

def find_multiple_zeros_newton(f,df,a,b):
    ans = []
    for i in np.arange(a,b,0.1):
        x = newton(f,df,i)
        if x[-1] not in ans:
            ans.append(x[-1])
    return ans

def s(x):
    return np.sin(x)

def ds(x):
    return np.cos(x)

def func(x):
    return np.exp(-2 * x) + 5 * x**2 - 7 * x

def dfunc(x):
    return -2 * np.exp(-2 * x) + 10 * x - 7

def error(x,accept):
    for i in range(0,len(x)):
        x[i] = abs(x[i] - accept)
    return x

accepted = 1.39110026186
plt.xlabel('iteration')
plt.ylabel('error in x value of root')
plt.plot(error(bisect(func,1,2),accepted), label = 'bisection')
plt.plot(error(newton(func,dfunc,1.5),accepted), label = 'newton')
plt.legend(loc='upper right')
plt.show()

print(find_multiple_zeros_bisect(s,-10,10))
print(find_multiple_zeros_newton(s,ds,0,3))