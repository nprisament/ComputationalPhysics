# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:21:55 2019

@author: npris
"""

import numpy as np
import matplotlib.pyplot as plt

def fd(f,h,x):
    return (f(x + h) - f(x)) / h

def cd(f,h,x):
    return (f(x + h/2) - f(x - h/2)) / h

def fivept(f,h,x):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h)  + f(x - 2*h)) / (12 * h)

def f1(x):
    return x**2

def df1(x):
    return 2 * x

def f2(x):
    return x**3

def df2(x):
    return 3 * x**2

def f3(x):
    return np.exp(-x)

def df3(x):
    return -f3(x)

def f4(x):
    return np.sin(x)

def df4(x):
    return np.cos(x)

def error(method, f, df, h, x):
    return abs(method(f,h,x) - df(x))

x = 1
h = np.logspace(-1,-16,16)
plt.figure(0)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('step size (h)')
plt.ylabel('error')

errorval = []
for i in h:
    errorval.append(error(fd,f1,df1,i,x))
plt.plot(h, errorval, label = 'forward diff')

errorval = []
for i in h:
    errorval.append(error(cd,f1,df1,i,x))
plt.plot(h, errorval, label = 'central diff')

errorval = []
for i in h:
    errorval.append(error(fivept,f1,df1,i,x))
plt.plot(h, errorval, label = '5pt')

plt.legend(loc='lower left')
plt.show()

h = np.logspace(-1,-16,16)
plt.figure(1)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('step size (h)')
plt.ylabel('error')

errorval = []
for i in h:
    errorval.append(error(fd,f2,df2,i,x))
plt.plot(h, errorval, label = 'forward diff')

errorval = []
for i in h:
    errorval.append(error(cd,f2,df2,i,x))
plt.plot(h, errorval, label = 'central diff')

errorval = []
for i in h:
    errorval.append(error(fivept,f2,df2,i,x))
plt.plot(h, errorval, label = '5pt')

plt.legend(loc='lower left')
plt.show()

h = np.logspace(-1,-16,16)
plt.figure(2)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('step size (h)')
plt.ylabel('error')

errorval = []
for i in h:
    errorval.append(error(fd,f3,df3,i,x))
plt.plot(h, errorval, label = 'forward diff')

errorval = []
for i in h:
    errorval.append(error(cd,f3,df3,i,x))
plt.plot(h, errorval, label = 'central diff')

errorval = []
for i in h:
    errorval.append(error(fivept,f3,df3,i,x))
plt.plot(h, errorval, label = '5pt')

plt.legend(loc='lower left')
plt.show()

h = np.logspace(-1,-16,16)
plt.figure(3)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('step size (h)')
plt.ylabel('error')

errorval = []
for i in h:
    errorval.append(error(fd,f4,df4,i,x))
plt.plot(h, errorval, label = 'forward diff')

errorval = []
for i in h:
    errorval.append(error(cd,f4,df4,i,x))
plt.plot(h, errorval, label = 'central diff')

errorval = []
for i in h:
    errorval.append(error(fivept,f4,df4,i,x))
plt.plot(h, errorval, label = '5pt')

plt.legend(loc='lower left')
plt.show()