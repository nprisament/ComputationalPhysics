# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:35:08 2019

@author: npris
"""
#the over-under relaxation method
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

size = 128
init = 0.0
boundary = 0
fixed = 10
beta = 1.5

tol = 0.5 #* 10**-1

def val(g):
    sum = 0
    for i in g:
        for j in i:
           sum += j
    return sum

def Q(i,j):
    x = math.ceil(size / 10)
    y = -x
    return ((i + 1 <= math.floor((size + 1) / 2) + x
        and i + 1 >= math.ceil((size + 1) / 2) + y) 
            and ((j + 1 <= math.floor((size + 1) / 2) + x
                and j + 1 >= math.ceil((size + 1) / 2) + y)))


def initGrid(lgrid):
    for i in range(0,size):
        lgrid.append([])
        for j in range(0,size):
            if (Q(i,j)):
                lgrid[i].append(fixed)
            else:
                lgrid[i].append(init)
    return lgrid

def relax(localBeta):
    grid = initGrid([])
    count = 0
    val0 = 0
    val1 = val(grid)
    while abs(val0 - val1) > tol:
        val0 = val1
        for i in range(0,size):
            for j in range(0,size):
                if (not Q(i,j)):
                    old = grid[i][j]
                    left = 0
                    right = 0
                    up = 0
                    down = 0
                    if (i != 0):
                        up = grid[i-1][j]
                    if (i != size - 1):
                        down = grid[i+1][j]
                    if (j != 0):
                        left = grid[i][j-1]
                    if (j != size - 1):
                        right = grid[i][j+1]
                    sum = left + right + up + down
                    grid[i][j] = sum / 4
                    grid[i][j] = localBeta * grid[i][j] + (1 - localBeta) * old
        val1 = val(grid)
        count += 1
    return grid, count

d = 0.01
betaVals = np.arange(1.5,2.0+d,d)

counts = []
for i in betaVals:
    grid, count = relax(i)
    counts.append(count)
    print(count)
    
plt.plot(betaVals, counts)
plt.ylabel("iterations")
plt.xlabel("beta")
plt.show()

#grid, count = relax(1.76)
#ax = sns.heatmap(grid, annot=False, xticklabels=False,
#                 yticklabels=False, linewidth=0.0, cmap="RdYlBu_r")
#plt.ylabel("y")
#plt.xlabel("x")
#plt.show()
#print(count)