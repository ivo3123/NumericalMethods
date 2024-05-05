'''
Задача 4

Дадена е функцията на Рунге 𝑓(𝑥)=1/(1+25*(x**2)).
Да се приближи 𝑓(𝑥) в интервала 𝑥∈[−1,1],
    като се използват интерполационни полиноми от степени 10 и 4 с равноотдалечени възли.
Да се построят графиките на всеки от полиномите,
    заедно с графиката на функцията в една координатна система,
        както и графиките на абсолютната грешка по модул в двата случая.
'''

import matplotlib.pyplot as plt
import numpy as np

from util.newton_poly import newton_poly

def runge(x):
    return 1 / (1 + 25 * (x ** 2))

nodes_degree_10 = np.linspace(-1, 1, 11)
nodes_degree_4 = np.linspace(-1, 1, 5)

values_degree_10 = np.array(runge(nodes_degree_10))
values_degree_4 = np.array(runge(nodes_degree_4))

x_axis = np.linspace(-1, 1, 1000)

plt.plot(x_axis, newton_poly(nodes_degree_10, values_degree_10, x_axis), label='deg_10', color='blue')
plt.plot(x_axis, newton_poly(nodes_degree_4, values_degree_4, x_axis), label='deg_4', color='green')
plt.plot(x_axis, runge(x_axis), label='runge', linestyle='dashed', color='orange')
plt.legend(['deg_10', 'deg_4', 'runge'])
plt.show()
