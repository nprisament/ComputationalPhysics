# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:37:14 2019

@author: npris
"""

from math import e
from numpy import arange

sum = 0
h = 1000000
for i in range(h + 1):
    w = 1
    if (i == 0 or i == h):
        w = 0.5
    sum += w * e**(i / h) / h
print(sum)


def integrate(func, a, b):
    sum = 0
    inc = (b - a) / 1000000
    for i in arange(a, b + inc, inc):
        w = 1
        if (i == a or i == b):
            w = 0.5
        sum += w * func(i) * inc
    return sum


print(integrate(lambda a: e**a, 1, 3))
