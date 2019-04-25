from random import *
import matplotlib.pyplot as plt

random_nums = []

for i in range(100):
	random_nums.append(random())

plt.figure(1)
plt.xlabel('i')
plt.ylabel('x_i')
plt.plot(random_nums)
plt.show()