# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:35:08 2019

@author: npris
"""
import math
import numpy as np
import matplotlib.pyplot as plt

dx = 0.1
dt = .001

rod = []
length = 5
tmax = 0.03
diffusivity = 5
eta = diffusivity * dt / dx**2
gamma = 0.0
room_temp = -1
I = math.floor(length / dx)
J = math.floor(tmax / dt)

rod.append([])
for i in np.arange(0,length,dx):
    rod[0].append(np.exp(-(i - length / 2)**2))

for j in range(1, J+1):
    rod.append([])
    for i in range(I):
        new = 0
        uij = rod[j-1][i]
        uimj = 0
        uipj = 0
        if (i != 0):
            uimj = rod[j-1][i-1]
        if (i != I - 1):
            uipj = rod[j-1][i+1]
        if (i != 0 and i != I - 1):
            new = uij + eta * (uimj + uipj - 2 * uij)
        elif (i == 0):
            new = uij + eta * 2 * (uipj - uij)
        else:
            new = uij + eta * 2 * (uimj - uij)
        new = new - gamma * (uij - room_temp)
        rod[j].append(new)

for j in range(J+1):
    plt.plot(np.arange(0,length,dx), rod[j]) 
plt.ylabel("Heat")
plt.xlabel("Position")
plt.show()