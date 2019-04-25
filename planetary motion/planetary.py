# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:42:07 2019

@author: npris
"""
import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt

def f(a,b):
    const = 1.32712440018* (10**20)
    r = np.sqrt(a**2 + b**2)
    return -const * a / r**3

def rk4(z, t, h):
    k1x = z[2]
    k1vx = f(z[0],z[1])
    k1y = z[3]
    k1vy = f(z[1],z[0])
    k2x = z[2] + 0.5 * h * k1vx
    k2vx = f(z[0] + 0.5 * h * k1x,z[1] + 0.5 * h * k1y)
    k2y = z[3] + 0.5 * h * k1vy
    k2vy = f(z[1] + 0.5 * h * k1y,z[0] + 0.5 * h * k1x)
    k3x = z[2] + 0.5 * h * k2vx
    k3vx = f(z[0] + 0.5 * h * k2x,z[1] + 0.5 * h * k2y)
    k3y = z[3] + 0.5 * h * k2vy
    k3vy = f(z[1] + 0.5 * h * k2y,z[0] + 0.5 * h * k2x)
    k4x = z[2] + h * k3vx
    k4vx = f(z[0] + h * k3x,z[1] + h * k3y)
    k4y = z[3] + h * k3vy
    k4vy = f(z[1] + h * k3y,z[0] + h * k3x)
    x = z[0] + h * (k1x + 2*k2x + 2*k3x + k4x) / 6
    y = z[1] + h * (k1y + 2*k2y + 2*k3y + k4y) / 6  
    vx = z[2] + h * (k1vx + 2*k2vx + 2*k3vx + k4vx) / 6
    vy = z[3] + h * (k1vy + 2*k2vy + 2*k3vy + k4vy) / 6
    return x, y, vx, vy         

h = 1
a = 10**9
b = 10**4

z = [0,1.521 * a, 29.8 * b,0]
N = 50000
xe = []
ye = []
t = 0
for i in range(N):
    t = i * h
    z = rk4(z, t, h)
    xe.append(z[0])
    ye.append(z[1])
    
plt.plot(xe, ye, color='green')

z = [0,8.166 * a,13.1 * b,0]
N = 500000
xj = []
yj = []
t = 0
for i in range(N):
    t = i * h
    z = rk4(z, t, h)
    xj.append(z[0])
    yj.append(z[1])

plt.plot(xj, yj, color='red')

plt.axis('equal')
plt.grid(True)
plt.show()