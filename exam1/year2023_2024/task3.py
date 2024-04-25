'''
Контролно 2023/2024г.
Вариант ?

задача 3

Дадена е таблица с възли и стойности:

възли        0.01   3        6        9          12
стойности    0.3    0.025    0.003    0.00008    0.0000032

Намерете обобщен полином, който интерполира данните, като използвате подходящ базис.
Илюстрирайте графично решението.
'''

import numpy as np
import matplotlib.pyplot as plt

nodes = np.array([0.01, 3, 6, 9, 12])
values = np.array([0.3, 0.025, 0.003, 0.00008, 0.0000032])

n = nodes.size

matrix = np.ones([n, n])

def basis(n, x):
    return 1 / (n + x + 1)

for row in range(n):
    for column in range(n):
        matrix[row, column] = basis(column, nodes[row])
        
vector_column = np.linalg.solve(matrix, values)

def exp_poly(params, x, basis):
    return sum(params[i] * basis(i, x) for i in range(params.size))

x_axis = np.linspace(0, 12, 1000)

plt.scatter(nodes, values)
plt.plot(x_axis, exp_poly(vector_column, x_axis, basis))
plt.show()