'''
Да се намери приближено стойността на sin(pi/5)
като за целта се построи интерпоалционният полином на Лагранж за функцията f(x) = sin(x) с възли:
x0 = 0
x1 = pi/6
x2 = pi/3
x3 = pi/2

Да се начертаят графиките на двете функции, заедно с точките на интерполация в една коориднатна система.
Да се направи оценка на грешката от така направеното приближение и да се сравни с абсолютната грешка.
'''

import numpy as np
import matplotlib.pyplot as plt
import math

from util.lagrange_poly import *

nodes = np.array([0, np.pi/6,  np.pi/3, np.pi/2])

def f(x):
    return np.sin(x)

def get_abs_error(function, interpolated_poly, nodes, values, x):
    return abs(function(x) - interpolated_poly(nodes, values, x))

# works for sin
def get_max_error(function, interpolated_poly, nodes, values, x):
    numerator = 1.0
    for i in range(nodes.size):
        numerator *= abs(x - nodes[i])

    denominator = math.factorial(nodes.size)

    return numerator / denominator

exact_value = f(np.pi/5)
approx_value = lagrange_poly(nodes, f, np.pi/5)
print("Exact value: ", exact_value)
print("Approx value: ", approx_value)
print("Absolute error: ", abs(exact_value - approx_value))
    
x_axis = np.linspace(0, np.pi/2, 1000)

plt.scatter(nodes, f(nodes), color='blue', marker='o', label='nodes')
plt.plot(x_axis, lagrange_poly(nodes, f, x_axis), label='IPL(x)', linestyle='dashed', color='black')
plt.plot(x_axis, f(x_axis), label='sin(x)', color='orange')
plt.legend(['data', 'Lagrange polynomial', 'sin(x)'])
plt.grid(False)
plt.gca().set_facecolor('white')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x) & Lagrange polynomial')
plt.show()

plt.plot(x_axis, get_abs_error(f, lagrange_poly, nodes, f, x_axis))
plt.plot(x_axis, get_max_error(f, lagrange_poly, nodes, f, x_axis))
plt.legend(['absolute error', 'max error'])
plt.show()