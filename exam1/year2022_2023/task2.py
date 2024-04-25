'''
Контролно 2022/2023г.
Вариант 3

задача 2

Да се приближи функцията f(x) = ln(x^3), като се построи полинома на Ермит с възли 0.2, 0.3 и съответни кратности 2 и 1.
Да се построи графиката на относителната грешка по абсолютна стойност в интервала на интерполация.
'''

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.log(x ** 3)

def f_prim(x):
    return 3 / x

nodes = np.array([0.2, 0.2, 0.3])
values = np.array([f(0.2), f_prim(0.2), f(0.3)])

def get_approporiate_derivative(nodes, values, l, r):
    for i in range(0, r+1):
        if nodes[i] == nodes[l]:
            return values[i + l - r]

def div_dif(nodes, values, l, r):
    if nodes[l] == nodes[r]:
        return get_approporiate_derivative(nodes, values, l ,r) / math.factorial(r-l)
    else:
        return (div_dif(nodes, values, l+1, r) - div_dif(nodes, values, l, r-1)) / (nodes[r] - nodes[l])


def hermit_poly(nodes, values, x):
    return sum(div_dif(nodes, values, 0, i) * (math.prod(x - nodes[j] for j in range(0, i))) for i in range(nodes.size))


x_axis = np.linspace(nodes.min(), nodes.max(), 100)

plt.scatter([0.2, 0.3], [f(0.2), f(0.3)])
plt.plot(x_axis, f(x_axis))
plt.plot(x_axis, hermit_poly(nodes, values, x_axis))
plt.legend(['points', 'f(x) = ln(x^3)', 'hermit_poly'])
plt.show()

def abs_error(nodes, values, x):
    return abs(f(x) - hermit_poly(nodes, values, x)) / abs(f(x))

plt.plot(x_axis, abs_error(nodes, values, x_axis))
plt.legend(['relative error'])
plt.show()

'''
The Hermit polinomial does not interpolate f(x) very well due to the few nodes.
If we added another node 0.3, then the approximation would be significanly more accurate.
'''