'''
Контролно 2022/2023г.
Вариант 3

задача 3

Да се дефинира функция Lagrange(n, A, B, f, x),
    която построява интерполационния полином на Лагранж от степен n на функцията f(x)
        с равноотдалечени възли в интервала [A, B], като използва формулата на Лагранж.
'''

import numpy as np
import matplotlib.pyplot as plt

def get_kth_lagrange(x, kth_index, nodes):
    result = 1.0
    
    for i in range(nodes.size):
        if i != kth_index:
            result *= (x - nodes[i]) / (nodes[kth_index] - nodes[i])
    return result
    
def lagrange_poly(n, A, B, f, x):
    nodes = np.linspace(A, B, n+1)  # n+1 points define a polnomial of degree n

    return sum(f(nodes[i]) * get_kth_lagrange(x, i, nodes) for i in range(nodes.size))


# test case
# not part of the solution

def k(x):
    return np.sin(2*x) + np.e ** np.cos(x)

x_axis = np.linspace(2, 10, 200)
plt.plot(x_axis, lagrange_poly(degree := 47, A := 2, B := 10, function := k, x_axis))
plt.plot(x_axis, k(x_axis))
plt.legend(['lagrange_poly', 'k(x)'])
plt.show()

'''
When we have lagrange poly of 47-th degree the approximation is really good.
However if we increase the degree to 67 for example
    the approximation is suddenly a lot worse due to the oscillations of polinomials of heigher degrees
'''    