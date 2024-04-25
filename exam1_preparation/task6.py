import numpy as np
import matplotlib.pyplot as plt

from util.lagrange_poly import lagrange_poly

def fake_lagrange_poly(degree, x0, h, function, x):
    return lagrange_poly(np.array([x0 + i * h for i in range(0, degree + 1)]), function, x)

nodes = np.array([0.3, 0.5, 0.9, 1.1, 1.2, 1.9])

x_axis = np.linspace(nodes.min(), nodes.max(), 200)

plt.scatter([nodes], [np.cos(nodes)])
plt.plot(x_axis, np.cos(x_axis))
plt.plot(x_axis, lagrange_poly(nodes, np.cos, x_axis))
plt.plot(x_axis, fake_lagrange_poly(8, 0.3, 0.2, np.cos, x_axis))
plt.legend(['points', 'cos', 'IPL', 'fake_IPL'])
plt.show()