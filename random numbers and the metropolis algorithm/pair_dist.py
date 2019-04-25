# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 04:20:01 2019

@author: npris
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

pair = []  
input_file = open('pair_dist.txt', 'r') 
for i in range(750):
    pair.append(float(input_file.readline()))

plt.figure(1)
plt.xlabel('r')
plt.ylabel('g(r)')
plt.plot(np.arange(0,7.5,0.01),pair, color='red')
plt.show()

x = []  
input_file2 = open('x_y.txt', 'r') 
for i in range(50):
    x.append(float(input_file2.readline()))
y = []  
for i in range(50):
    y.append(float(input_file2.readline()))
z = []  
for i in range(50):
    z.append(float(input_file2.readline()))

plt.figure(2)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x,y,z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter(x,y,z, color='red')

plt.show()

#gas 1.7 -4.81136
#liquid 0.3 -6.38151
#solid 0.02 -26.7715