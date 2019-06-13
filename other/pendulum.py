import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode

alpha = 1
b = 20
omega = 1
L = .1

def fun(t, z):
    """
    Right hand side of the differential equations
      dx/dt = -omega * y
      dy/dt = omega * x
    """
    theta, dtheta = z
    f = [dtheta, (-9.8/L) * np.sin(theta) - alpha * dtheta + b * np.cos(omega * t) ]
    return f

solver = ode(fun)
solver.set_integrator('dopri5', nsteps=45)


t0 = 0.0
z0 = [0,0]#1.5*10**8, 3*10**10, 0]
solver.set_initial_value(z0, t0)

t1 = 30
N = math.floor(75 * (t1/2.5))
t = np.linspace(t0, t1, N)
sol = np.empty((N, 2))
sol[0] = z0

k = 1
while solver.successful() and solver.t < t1:
    solver.integrate(t[k])
    sol[k] = solver.y
    k += 1

# Plot the solution...
plt.plot(t, sol[:,0], label='x')
plt.plot(t, sol[:,1], label='y')
plt.xlabel('t')
plt.grid(True)
plt.legend()
plt.show()

plt.plot(np.sin(sol[:,0]) * L,L - np.cos(sol[:,0]) * L)
plt.xlim([-L,L])
plt.ylim([0,L])
plt.grid(True)
plt.show()