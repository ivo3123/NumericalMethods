import numpy as np
import matplotlib.pyplot as plt

from util.tschebyscheff import get_tschebyscheff_nodes
from util.lagrange_poly import lagrange_poly

def f(x):
    return np.cos(2*x) * (x ** 2 - 0.2)

nodes = np.array([-1, -0.7, -0.3, 0.3, 0.7, 1])
degree = nodes.size - 1

tschebyscheff_nodes = get_tschebyscheff_nodes(degree)

x_axis = np.linspace(nodes.min(), nodes.max(), 200)

plt.plot(x_axis, f(x_axis))
plt.plot(x_axis, lagrange_poly(nodes, f, x_axis))
plt.plot(x_axis, lagrange_poly(tschebyscheff_nodes, f, x_axis))
plt.legend(['f(x)', 'lagrange_poly_original_nodes', 'lagrange_poly_tschebyscheff_nodes'])
plt.show()

def get_signless_absolute_error(function, iterpolating_function, nodes, values, x):
    return abs(function(x) - iterpolating_function(nodes, values, x))

plt.plot(x_axis, get_signless_absolute_error(f, lagrange_poly, nodes, f, x_axis))
plt.plot(x_axis, get_signless_absolute_error(f, lagrange_poly, tschebyscheff_nodes, f, x_axis))
plt.legend(['original_nodes', 'tschebyscheff_nodes'])
plt.show()
