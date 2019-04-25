import numpy as np
import matplotlib.pyplot as plt

def f(a, b, c, d, j):
    const = 1.32712440018* (10**11)
    r = np.sqrt(a**2 + b**2)
    
    constp = 1.26686534 * 1000 * (10**8)
    if (j):
        constp = 3.986004418* (10**5)    
    dj = np.abs(a - c)
    rj = np.sqrt((a-c)**2 + (b-d)**2)
    interaction = -constp * dj / rj**3
    interaction = 0 #for non-interation

    return (-const * a / r**3) + interaction

def rk4(z, z2, t, h, j):
    k1x = z[2]
    k1vx = f(z[0],z[1], z2[0], z2[1], j)
    k1y = z[3]
    k1vy = f(z[1],z[0], z2[1], z2[0], j)
    k2x = z[2] + 0.5 * h * k1vx
    k2vx = f(z[0] + 0.5 * h * k1x,z[1] + 0.5 * h * k1y, z2[0], z2[1], j)
    k2y = z[3] + 0.5 * h * k1vy
    k2vy = f(z[1] + 0.5 * h * k1y,z[0] + 0.5 * h * k1x, z2[1], z2[0], j)
    k3x = z[2] + 0.5 * h * k2vx
    k3vx = f(z[0] + 0.5 * h * k2x,z[1] + 0.5 * h * k2y, z2[0], z2[1], j)
    k3y = z[3] + 0.5 * h * k2vy
    k3vy = f(z[1] + 0.5 * h * k2y,z[0] + 0.5 * h * k2x, z2[1], z2[0], j)
    k4x = z[2] + h * k3vx
    k4vx = f(z[0] + h * k3x,z[1] + h * k3y, z2[0], z2[1], j)
    k4y = z[3] + h * k3vy
    k4vy = f(z[1] + h * k3y,z[0] + h * k3x, z2[1], z2[0], j)
    x = z[0] + h * (k1x + 2*k2x + 2*k3x + k4x) / 6
    y = z[1] + h * (k1y + 2*k2y + 2*k3y + k4y) / 6  
    vx = z[2] + h * (k1vx + 2*k2vx + 2*k3vx + k4vx) / 6
    vy = z[3] + h * (k1vy + 2*k2vy + 2*k3vy + k4vy) / 6
    return x, y, vx, vy         

h = 1
a = 10**6

z1 = [0, 1.521 * a, 298, 0]
z2 = [0, 8.166 * a, 131, 0]
N = 1000000
xe = []
ye = []
xj = []
yj = []
t = 0
for i in range(N):
    t = i * h
    z1 = rk4(z1, z2, t, h, False)
    z2 = rk4(z2, z1, t, h, True)
    xe.append(z1[0])
    ye.append(z1[1])
    xj.append(z2[0])
    yj.append(z2[1])

periodse = []
periodsj = []
sume = 0
sumj = 0
for i in range(N):
    sume = sume + 1
    if (ye[i - 1] > 0 and ye[i] < 0):
        periodse.append(sume)
        sume = 0
    sumj = sumj + 1
    if (yj[i - 1] > 0 and yj[i] < 0):
        periodse.append(sumj)
        sumj = 0

sume = 0
for i in periodse:
    sume = sume + i
periode = sume / len(periodse)
sumj = 0
for i in periodsj:
    sumj = sumj + i
#periodj = sumj / len(periodsj)

plt.plot(xe, ye, color='green', label='Earth')    
plt.plot(xj, yj, color='red', label='Jupiter')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()

print("Earth periodicity:")
print(periode)
#print(periodj)