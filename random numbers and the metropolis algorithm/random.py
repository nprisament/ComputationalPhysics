# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 01:24:30 2019

@author: npris
"""

from functools import *
from random import *
import numpy as np
import matplotlib.pyplot as plt

N = 10000
random_nums = []

for i in range(N):
	random_nums.append(random())

plt.figure(1)
plt.xlabel('i')
plt.ylabel('x_i')
plt.scatter(range(N),random_nums, s=0.1)
plt.show()

k = 5
x = random_nums[0:N-k]
y = random_nums[k:N]
plt.figure(2)
plt.xlabel('i')
plt.ylabel('x_i')
plt.scatter(x,y, s=0.1)
plt.show()

def moment(k_loc):
    return reduce((lambda x, y: x + y), map(lambda x: x**k_loc, random_nums)) / N
  
for k in range(6):
    print(k,"th moment:",moment(k))
    print(k,"th moment theoretical:",(1/(k+1)))
print("\n")

def correlation(k_loc):
    mults = []
    for i in range(len(random_nums) - k):
        mults.append(random_nums[i] * random_nums[i + k])
    return reduce((lambda x, y: x + y), mults) / N

for k in range(6):
    print(k,"th correlation:",correlation(k))
    print(k,"th correlation theoretical:",1 / 4)
print("\n")

plt.figure(3)
plt.xlabel('bins')
plt.ylabel('frequency')
plt.hist(random_nums, bins=10)
plt.show()

for i in range(N):
	random_nums[i] = 1 - random_nums[i]

plt.figure(4)
plt.xlabel('i')
plt.ylabel('x_i')
plt.scatter(range(N),random_nums, s=0.1)
plt.show()

k = 5
x = random_nums[0:N-k]
y = random_nums[k:N]
plt.figure(5)
plt.xlabel('i')
plt.ylabel('x_i')
plt.scatter(x,y, s=0.1)
plt.show()

def moment(k_loc):
    return reduce((lambda x, y: x + y), map(lambda x: x**k_loc, random_nums)) / N
  
for k in range(6):
    print(k,"th moment:",moment(k))
    print(k,"th moment theoretical:",(1/(k+1)))
print("\n")

def correlation(k_loc):
    mults = []
    for i in range(len(random_nums) - k):
        mults.append(random_nums[i] * random_nums[i + k])
    return reduce((lambda x, y: x + y), mults) / N

for k in range(6):
    print(k,"th correlation:",correlation(k))
    print(k,"th correlation theoretical:",1 / 4)
print("\n")

plt.figure(6)
plt.xlabel('bins')
plt.ylabel('frequency')
plt.hist(random_nums, bins=10)
plt.show()

randorg = []  
input_file = open('random.txt', 'r') 
for i in range(N):
    randorg.append(float(input_file.readline()))

plt.figure(7)
plt.xlabel('i')
plt.ylabel('x_i')
plt.scatter(range(N),randorg, s=0.1)
plt.show()

k = 5
x = randorg[0:N-k]
y = randorg[k:N]
plt.figure(8)
plt.xlabel('i')
plt.ylabel('x_i')
plt.scatter(x,y, s=0.1)
plt.show()

def moment2(k_loc):
    return reduce((lambda x, y: x + y), map(lambda x: x**k_loc, randorg)) / N

for k in range(6):
    print(k,"th moment:",moment2(k))
    print(k,"th moment theoretical:",(1/(k+1)))
print("\n")

def correlation2(k_loc):
    mults = []
    for i in range(len(randorg) - k):
        mults.append(randorg[i] * randorg[i + k])
    return reduce((lambda x, y: x + y), mults) / N

for k in range(6):
    print(k,"th correlation:",correlation2(k))
    print(k,"th correlation theoretical:",1 / 4)
print("\n")

plt.figure(9)
plt.xlabel('bins')
plt.ylabel('frequency')
plt.hist(randorg, bins=10)
plt.show()




