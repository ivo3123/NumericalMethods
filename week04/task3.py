'''
Задача 3

Да се имплементира функция newton_forward(n, x0, h, f),
    която построява интерполационния полином на Лагранж от степен 𝑛 за функцията 𝑓(𝑥) с възли 𝑥𝑖=𝑥0+𝑖ℎ,𝑖=0,…,𝑛
        ,като използва формулата на Нютон за интерполиране напред.
'''

import numpy as np
import matplotlib.pyplot as plt

from util.newton_forward_poly import newton_forward_poly

def f(x):
    return x**3 - x - 9 + np.sin(np.cos(x**2))

x_axis = np.linspace(2, 3.6, 1000)

plt.plot(x_axis, f(x_axis), linestyle='dashed')
plt.plot(x_axis, newton_forward_poly(2, 0.1, 17, f, x_axis))
plt.legend(['f(x)', 'newton_forward'])
plt.show()