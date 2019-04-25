# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 01:25:32 2019

@author: npris
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

box_size = 3
dxdy = 0.03
size = math.floor(box_size / dxdy)

def V(x,y):
    return x**4 + y**4

h_x = np.eye(size)
for i in range(size):
    if (i > 0):
        h_x[i,i-1] = -1
    if (i < size - 1):
        h_x[i,i+1] = -1
    h_x[i,i] = 2

hamiltonian = np.kron(np.eye(size), h_x)
for i in range (size**2):
    if (i - size > -1):
        hamiltonian[i][i - size] = -1
    if (i + size < size**2):
        hamiltonian[i][i + size] = -1
    hamiltonian[i][i] += 2

for i in range(size):
    for j in range(size):
        pos = i + j * size
        hamiltonian[pos][pos] += V(i*dxdy - box_size / 2,j*dxdy - box_size / 2)

energies, wavefunctions = np.linalg.eigh(hamiltonian)

for x in range(50):
    grid = []
    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[i].append(wavefunctions[i + j * size,x])
    ax = sns.heatmap(grid, annot=False, xticklabels=False,
                     yticklabels=False, linewidth=0.0, cmap="RdYlBu_r")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()
    print(energies[x])
