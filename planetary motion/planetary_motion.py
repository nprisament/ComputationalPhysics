import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode


def fun(t, z):
    """
    Right hand side of the differential equations
      dx/dt = -omega * y
      dy/dt = omega * x
    """
    const = 5#6.67408 * 1.989 #*10**19
    x, y, dx, dy = z
    r = np.sqrt(x**2 + y**2)
    f = [dx, dy, -const * x / r**3, -const * y / r**3]
    return f

solver = ode(fun)
solver.set_integrator('dopri5', nsteps=45)


t0 = 0.0
z0 = [0, .05, 10, 0]#1.5*10**8, 3*10**10, 0]
solver.set_initial_value(z0, t0)

t1 = 50
N = math.floor(75 * (t1/2.5))
t = np.linspace(t0, t1, N)
sol = np.empty((N, 4))
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

plt.plot(sol[:,0], sol[:,1])
plt.grid(True)
plt.show()