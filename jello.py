# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

c = 0.01
dt = 0.5
dx = .01
eta = c**2 * dt**2 / dx**2
length = 0.75
size = math.floor(length / dx)
t_max = 1000
J = math.floor(t_max / dt)
interval = 100
mod = math.floor(interval / dt)

u = []
u.append([])
for x in range(size):
    u[0].append([])
    for y in range(size):
        u[0][x].append([])
        for z in range(size):
            u[0][x][y].append(0)
u.append([])
for x in range(size):
    u[1].append([])
    for y in range(size):
        u[1][x].append([])
        for z in range(size):
            #if (x > size * 3 / 8 and y > size * 3 / 8 and z > size * 3 / 8
             #   and x < size * 5 / 8 and y < size * 5 / 8 and z < size * 5 / 8):
              #  u[1][x][y].append(4)
            if (z == 0):
                u[1][x][y].append(10)
            else:   
                u[1][x][y].append(0)

for j in range(2, J+1):
    u.append([])
    for x in range(size):
        u[j].append([])
        for y in range(size):
            u[j][x].append([])
            for z in range(size):
                if (z == 0 and j % mod == 0):
                    u[j][x][y].append(10)
                    continue
                new = 0
                uj = u[j-1][x][y][z]
                ujm = u[j-2][x][y][z]
                uxpj = 0
                if (x != size - 1):
                    uxpj = u[j-1][x+1][y][z]
                uxmj = 0
                if (x != 0):
                    uxmj = u[j-1][x-1][y][z]
                uypj = 0
                if (y != size - 1):
                    uypj = u[j-1][x][y+1][z]
                uymj = 0
                if (y != 0):
                    uymj = u[j-1][x][y-1][z]
                uzpj = 0
                if (z != size - 1):
                    uzpj = u[j-1][x][y][z+1]
                uzmj = 0
                if (z != 0):
                    uzmj = u[j-1][x][y][z-1]
                laplacian = uxpj + uxmj + uypj + uymj + uzpj + uzmj - 6 * uj
                new = 2 * uj - ujm + eta * (laplacian)
                u[j][x][y].append(new)
    if (j % 2 == 0):
        ax = sns.heatmap(u[j][math.floor(size / 2)], annot=False, xticklabels=False,
                     yticklabels=False, linewidth=0.0, cmap="RdYlBu_r", vmin=-25, vmax=25)
        plt.ylabel("z")
        plt.xlabel("y")
        plt.show()