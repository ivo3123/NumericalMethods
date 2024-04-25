import numpy as np
import matplotlib.pyplot as plt

from util.hermit_poly import hermit_poly

def f(x):
    return np.sin(x ** 2) ** 3

def f_der1(x):
    return 6 * x * np.cos(x ** 2) * (np.sin(x ** 2) ** 2)

def f_der2(x):
    return 6 * np.sin(x ** 2) * (np.sin(x ** 2) * np.cos(x ** 2) + 4 * (x ** 2) * (np.cos(x ** 2) ** 2) - 2 * (x ** 2) * (np.sin(x ** 2) ** 2))


nodes = np.array([np.pi/6, np.pi/6, np.pi/5, np.pi/5, np.pi/5])
values = np.array([f(nodes[0]), f_der1(nodes[1]), f(nodes[2]), f_der1(nodes[3]), f_der2(nodes[4])])

x_axis = np.linspace(0.3, 0.9, 300)

plt.scatter([np.pi/6, np.pi/5], [f(np.pi/6), f(np.pi/5)])
plt.plot(x_axis, hermit_poly(nodes, values, x_axis))
plt.plot(x_axis, f(x_axis))
plt.legend(['points', 'hermit_poly', 'f'])
plt.show()