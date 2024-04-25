import numpy as np
import matplotlib.pyplot as plt

from util.basis_poly import basis_poly

nodes = np.array([0, 2, 4, 6, 8])
values = np.array([0.1, 0.009, 0.0011, 0.00003, 0.0000012])

x_axis = np.linspace(0, 8, 300)

plt.scatter(nodes, values)
plt.plot(x_axis, basis_poly(nodes, values, x_axis, lambda x, n: 1 / (n + x + 1)))
plt.show()