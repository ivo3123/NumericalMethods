'''
Контролно 2023/2024г.
Вариант ?

задача 2

Да се приближи функцията f(x) = e^x, като се построи полинома на Ермит с възли 0, 1 и съответни кратности 2 и 2.
Да се изведе стойността на построения полином в точката x = 0.5 и да се изведе грешката спрямо f(0.5).
'''

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.e ** x

def f_der1(x):
    return f(x)

nodes = np.array([0, 0, 1, 1])
values = np.array([f(0), f_der1(0), f(1), f_der1(1)])

n = nodes.size

def get_value(nodes, values, l, r):
    for i in range(0, r + 1):
        if nodes[i] == nodes[l]:
            return values[i + r - l]
    
    return None

def div_dif(nodes, values, l, r):
    if nodes[l] == nodes[r]:
        return get_value(nodes, values, l, r) / math.factorial(r - l)
    else:
        return (div_dif(nodes, values, l + 1, r) - div_dif(nodes, values, l, r - 1)) / (nodes[r] - nodes[l])

def hermit_poly(nodes, values, x):
    return sum(div_dif(nodes, values, 0, i) * (math.prod(x - nodes[j] for j in range(0, i))) for i in range(n))

real_value = f(0.5)
approx_value = hermit_poly(nodes, values, 0.5)
error = abs(real_value - approx_value)
print('real value is', real_value)
print('approx value is', approx_value)
print('abs error is', error)

visual_nodes = np.array([0, 1])
visual_values = np.array([f(0), f(1)])

x_axis = np.linspace(nodes.min(), nodes.max(), 200)

plt.scatter(visual_nodes, visual_values)
plt.plot(x_axis, f(x_axis), color='green', linestyle='dashed')
plt.plot(x_axis, hermit_poly(nodes, values, x_axis), color='orange')
plt.legend(['points', 'f(x) = e^x', 'hermit poly'])
plt.show()