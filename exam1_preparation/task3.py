import numpy as np
import matplotlib.pyplot as plt

from util.lagrange_poly import lagrange_poly
from util.hermit_poly import hermit_poly

def f(x):
    return np.cos(x)

lagrange_nodes = np.array([0, np.pi/4, np.pi/2])

hermit_nodes = np.array([0, 0, np.pi/2])
hermit_values = np.array([1, 0, 0])

x_axis = np.linspace(0, np.pi/2, 350)

plt.plot(x_axis, lagrange_poly(lagrange_nodes, f, x_axis), color='red')
plt.plot(x_axis, hermit_poly(hermit_nodes, hermit_values, x_axis), color='green')
plt.plot(x_axis, f(x_axis), color='blue', linestyle='dashed')
plt.legend(['Lagrange_IP(x)', 'Hermitit_IP(x)', 'cos(x)'])
plt.show()

def get_signless_absolute_error(function, iterpolating_function, nodes, values, x):
    return abs(function(x) - iterpolating_function(nodes, values, x))

plt.plot(x_axis, get_signless_absolute_error(f, lagrange_poly, lagrange_nodes, f, x_axis), color='red')
plt.plot(x_axis, get_signless_absolute_error(f, hermit_poly, hermit_nodes, hermit_values, x_axis), color='green')
plt.legend(['Абсолютна грешка от инт. п-м на Лагранж', 'Абсолютна грешка от инт. п-м на Ермит'])
plt.show()