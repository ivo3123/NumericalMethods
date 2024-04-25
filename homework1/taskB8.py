'''
HW1_B.pdf
задача 8

x    0.4    0.8    1.2     1.6     2       2.3
y    800    975    1500    1960    2900    3600

По метода на най-малките квадрати да се приближат данните от таблицата с фунцкия от вида:
y = a * (10 ^ (b * x))
За целта да се използва подходяща линеаризация на модела.
Да се визуализира полученото приближение, заедно с данните в една координатна система.
'''

import numpy as np
import matplotlib.pyplot as plt

nodes = np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3])
values = np.array([800, 975, 1500, 1960, 2900, 3600])

def mnmk_matrix_function(x, y, degree):
    if x.size != y.size:
        raise ValueError('The size of the two arrays should be equal')
    if degree < 0:
        raise ValueError('The degree should not be negative')
    
    points_count = x.size
    n = degree + 1

    # We create the vector of values of the right side of the equation
    values_vector_column = np.array([sum(y[i] * (x[i] ** s) for i in range(points_count)) for s in range(n)])

    # We create the matrix
    matrix = np.ones([n, n])
    for row in range(n):
        for column in range(n):
            matrix[row, column] = sum(x[i] ** (row + column) for i in range(points_count))

    # We solve the vector column of the left side of the equation to the right of the matrix,
    # containing all the coefficients of the desired polinom
    return np.linalg.solve(matrix, values_vector_column)

def hw1_B_task8_func(a, b, x):
    return a * 10 ** (b * x)

'''
y = a * 10 ** (b * x)
~~
y* = c + b * x
    where y* = log10(y) and c = log10(a)

This way we can find the values of a and b
as we can use the mnmk_function to find the coefficients of a linear equation
and the linear equation we will use is the one rewritten above
'''

c, b = mnmk_matrix_function(nodes, np.log10(values), degree_of_linear_functions := 1)

# log10(a) == c  <=>  a == c ** 10
a = 10 ** c

x_axis = np.linspace(nodes.min(), nodes.max(), 200)

plt.scatter(nodes, values, color='orange')
plt.plot(x_axis, hw1_B_task8_func(a, b, x_axis), color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Функция от вида y = a * 10^(b * x)')
plt.legend(['данните', 'функцията'])
plt.show()