'''
Контролно 2022/2023г.
Вариант 3

задача 1

В таблицата са представени данни за броя на заразените от дадено инфекциозно заболяване в един град, в течение на 5 седмици
поредна седмица    1    2      3      4       5
брой заразени      3    128    115    1050    13500
Намерете обобщен полином, който интерполира данните, като използвате подходящ базис.
Илюстрирайте графично решението.
Примерните базиси са:
{1, x, x^2, ..., x^n}
{1, e^x, e^(2*x), ..., e^(n*x)}
{1, sin(x), cos(x), ..., sin(n*x), cos(n*x)}
{1, e^(-x), e^(-2*x), ..., e^(-n*x)}
'''

import numpy as np
import matplotlib.pyplot as plt

nodes = np.array([1, 2, 3, 4, 5])
values = np.array([3, 125, 115, 1050, 13500])

def basis(x, n):
    return np.e ** (n * x)

n = nodes.size

matrix = np.ones([n, n])

for row in range(n):
    for column in range(n):
        matrix[row, column] = np.e ** (nodes[row] * column)

vars = np.linalg.solve(matrix, values)

def my_exp_poly(x):
    return sum(vars[i] * np.e ** (i * x) for i in range(n))

x_axis = np.linspace(nodes.min(), nodes.max(), 200)

plt.scatter(nodes, values)
plt.plot(x_axis, my_exp_poly(x_axis))
plt.legend(['points', 'poly'])
plt.show()