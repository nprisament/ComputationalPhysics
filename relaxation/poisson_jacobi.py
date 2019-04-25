# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:35:08 2019

@author: npris
"""
#the jacobi method
import math
import matplotlib.pyplot as plt
import seaborn as sns

size = 50
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

grids = []        
grid = []
for i in range(0,size):
    grid.append([])
    for j in range(0,size):
        if (Q(i,j)):
            grid[i].append(fixed)
        else:
            grid[i].append(init)
grids.append(grid)

grid = []
for i in range(0,size):
    grid.append([])
    for j in range(0,size):
        if (Q(i,j)):
            grid[i].append(fixed)
        else:
            left = 0
            right = 0
            up = 0
            down = 0
            if (i != 0):
                up = grids[0][i-1][j]
            if (i != size - 1):
                down = grids[0][i+1][j]
            if (j != 0):
                left = grids[0][i][j-1]
            if (j != size - 1):
                right = grids[0][i][j+1]
            sum = left + right + up + down
            grid[i].append(sum / 4)
grids.append(grid)

vals = []
vals.append(val(grids[-1]))
count = 0      
while abs(val(grids[-1]) - val(grids[-2])) > tol:
    grid = []
    for i in range(0,size):
        grid.append([])
        for j in range(0,size):
            if (Q(i,j)):
                grid[i].append(fixed)
            else:
                left = 0
                right = 0
                up = 0
                down = 0
                if (i != 0):
                    up = grids[-1][i-1][j]
                if (i != size - 1):
                    down = grids[-1][i+1][j]
                if (j != 0):
                    left = grids[-1][i][j-1]
                if (j != size - 1):
                    right = grids[-1][i][j+1]
                sum = left + right + up + down
                grid[i].append(sum / 4)
    count += 1
    print(count)
    vals.append(val(grids[-1]))
    grids.append(grid)
                
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