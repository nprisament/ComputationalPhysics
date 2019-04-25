from scipy import integrate
import numpy

alpha = 5
b = 0
omega = 10 
L = 1

def update (t, state):
	state_up = [0,0]
	state_up[0] = state[1]
	state_up[1] = (-9.8/L) * numpy.sin(state[0]) - alpha * state[1] + b * numpy.cos(omega * t) 
	return state_up
rk = integrate.RK45(update,0,[30,0], 50, 0.001)
for i in range(10000):
    rk.step()
    print(rk.y[0])
