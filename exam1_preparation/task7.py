import numpy as np
import matplotlib.pyplot as plt

from util.basis_poly import *
from util.lagrange_poly import lagrange_poly

nodes = np.array([0.95, 1.75, 4.75, 5.9])
values = np.array([10.3, 0.5, 0.9, 1.2])

'''
The nodes are sparsely located.
This means that interpolating directly may not give the best results.

To construct a periodic function we will need to use a trigonometric polinomial.

Let's plot an algebraic polynomial and a trigonometric and see the differences
'''

x_axis = np.linspace(nodes.min(), nodes.max(), 300)

plt.scatter(nodes, values)
plt.plot(x_axis, trig_poly(nodes, values, x_axis))
plt.plot(x_axis, alg_poly(nodes, values, x_axis))
plt.legend(['points', 'trig_poly', 'alg_poly'])
plt.show()

'''
The algebraic polynomial seems to interpolate the date much better.
So we will force the trigonometric polynomial to pass into some of the points, defined by the algebraic polynomial
'''

new_nodes = np.array([0.95, 1.75, 2.35, 3.05, 3.85, 4.75, 5.9])
new_values = np.array([10.3, 0.5, alg_poly(nodes, values, 2.35), alg_poly(nodes, values, 3.05), alg_poly(nodes, values, 3.85), 0.9, 1.2])

x_axis = np.linspace(nodes.min() - 2*np.pi, nodes.max() + 2*np.pi, 300)

plt.scatter(nodes, values)
plt.scatter([2.35, 3.05, 3.85], [alg_poly(nodes, values, 2.35), alg_poly(nodes, values, 3.05), alg_poly(nodes, values, 3.85)])
plt.plot(x_axis, trig_poly(nodes, values, x_axis))
plt.plot(x_axis, trig_poly(new_nodes, new_values, x_axis))
plt.legend(['initial points', 'added points', 'initial_trig_poly', 'corrected_trig_poly'])
plt.show()