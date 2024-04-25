'''
HW1_А.pdf
задача 8

x    0.75   2       3    4      6      8      8.5
y    1.2    1.95    2    2.4    2.4    2.7    2.6

По метода на най-малките квадрати да се приближат данните от таблицата с фунцкия от вида:
y = ( x / (d + x) ) * c
За целта да се използва подходяща линеаризация на модела.
Да се визуализира полученото приближение, заедно с данните в една координатна система.
'''

import numpy as np
import matplotlib.pyplot as plt

nodes = np.array([0.75, 2, 3, 4, 6, 8, 8.5])
values = np.array([1.2, 1.95, 2, 2.4, 2.4, 2.7, 2.6])

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

def desired_parabola(x):
    return polinom_of_degree(x, degree_of_parabola := 2)

def polinom_of_degree(x, degree):
    coefficients = mnmk_matrix_function(nodes, values, degree)
    return sum(coefficients[i] * x ** i for i in range(coefficients.size))

x_axis = np.linspace(nodes.min() - 1, nodes.max() + 1, 200)

plt.scatter(nodes, values, color='orange')
plt.plot(x_axis, desired_parabola(x_axis), color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Парабола, описваща данните, получена по МНМК')
plt.legend(['data', 'parabola'])
plt.show()