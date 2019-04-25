# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:35:08 2019

@author: npris
"""
#the gauss-seidel method
import math
import matplotlib.pyplot as plt
import seaborn as sns

size = 128
init = 0.0
boundary = 0
fixed = 10

tol = 0.5 * 10**-6

def val(g):
    sum = 0
    for i in g:
        for j in i:
           sum += j
    return sum

def Q(i,j):
    x = math.ceil(size / 8)
    y = -x
    return ((i + 1 <= math.floor((size + 1) / 2) + x
        and i + 1 >= math.ceil((size + 1) / 2) + y) 
            and ((j + 1 <= math.floor((size + 1) / 2) + x
                and j + 1 >= math.ceil((size + 1) / 2) + y)))

grid = []
for i in range(0,size):
    grid.append([])
    for j in range(0,size):
        if (Q(i,j)):
            grid[i].append(fixed)
        else:
            grid[i].append(init)
vals = []
count = 0
val0 = 0
val1 = val(grid)
vals.append(val1)
while abs(val0 - val1) > tol:
    val0 = val1
    for i in range(0,size):
        for j in range(0,size):
            if (not Q(i,j)):
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
                grid[i][j]= sum / 4
    val1 = val(grid)
    vals.append(val1)
    count += 1

ax = sns.heatmap(grid, annot=False, xticklabels=False,
                 yticklabels=False, linewidth=0.0, cmap="RdYlBu_r")
plt.ylabel("y")
plt.xlabel("x")
plt.show()

for i in range(len(vals)):
    vals[i] = abs(vals[i] - val1)

plt.plot(vals)
plt.ylabel("error")
plt.xlabel("iterations")
plt.show()

print(count)