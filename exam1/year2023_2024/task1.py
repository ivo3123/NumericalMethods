'''
Контролно 2023/2024г.
Вариант ?

задача 1

Дадена е функцията f(x) = ln(x^2 + 4).
Разполагаме с 4 равноотдалечени възли в интервала [0.1, 0.4].

Да се построи интерполационния полином на Лагранж.
Да се намери стойността на интерполирания полином в точката x=0.25
    и да се намери грешката с f(0.25) (по абсолютна стойност)
'''

import numpy as np
import matplotlib.pyplot as plt
import math

nodes = np.linspace(0.1, 0.4, 4)

n = nodes.size

def f(x):
    return np.log(x ** 2 + 4)

def kth_lagrange_poly(nodes, x, k):
    return math.prod((x - nodes[i]) / (nodes[k] - nodes[i]) if i != k else 1 for i in range(n))

def lagrange_poly(nodes, f, x):
    return sum(f(nodes[k]) * kth_lagrange_poly(nodes, x, k) for k in range(n))

real_value = f(0.25)
approx_value = lagrange_poly(nodes, f, 0.25)
error = abs(real_value - approx_value)
print('real value is', real_value)
print('approx value is', approx_value)
print('abs error is', error)

x_axis = np.linspace(nodes.min(), nodes.max(), 300)

plt.scatter(nodes, f(nodes))
plt.plot(x_axis, f(x_axis), color='green', linestyle='dashed')
plt.plot(x_axis, lagrange_poly(nodes, f, x_axis), color='orange')
plt.legend(['nodes', 'f(x) = ln(x^2 + 4)', 'lagrange_poly'])
plt.show()