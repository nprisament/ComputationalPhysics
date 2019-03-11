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
    return np.exp(x)

def df3(x):
    return f3(x)

def error(method, f, df, h, x):
    return abs(method(f,h,x) - df(x))

x = 1
h = np.logspace(-1,-16,16)
y = []
for i in h:
    y.append(error(fd,f1,df1,i,x))

plt.plot(h, y, 'ro')
plt.axis([10**-16, 10**-1, 0, 2])
plt.xscale('log')
plt.yscale('log')
plt.show()