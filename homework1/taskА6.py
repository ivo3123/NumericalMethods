'''
HW1_А.pdf
задача 6

x    0.5     1      2      3      4
y    10.4    5.8    3.3    2.4    2

Известно е, че данните от таблицата могат да бъдат моделирани чрез следната връзка:
y = ( (a + sqrt(x)) / (b*x) ) ^ 2
Да се линеаризира модела, като се използва подходяща трансформация.
По метода на най-малките квадрати да се определят стойностите на параметрите a и b.
Да се пресметне приближено стойността на y при x = 1.6.
Да се визуализира.
'''

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from sympy import symbols, diff, Eq, solve

nodes = np.array([0.5, 1, 2, 3, 4])
values = np.array([10.4, 5.8, 3.3, 2.4, 2])

'''
y = ((a + sqrt(x)) / (b * x)) ^ 2
<=>
yi = ((a + sqrt(xi)) / (b * xi)) ^ 2
~~
sqrt(yi) = A * (1/x) + B * (1/sqrt(x)) = f(x)
    where A = a/b and B = 1/b

and we want to minimize phi where
phi = sum((A * (1/xi) + B * (1/sqrt(xi))) - sqrt(yi)) for i from 0 to nodes/values.size
minimization is done with taking the derivative
'''

def hw1_A_task6_func(a, b, x):
    return ((a + np.sqrt(x)) / (b * x)) ** 2

A, B = symbols('A, B')
def f(A, B, x):
    return A * (1 / x) + B * (1 / np.sqrt(x))

def phi(A, B):
    sum_of_squares = 0
    for i in range(nodes.size):
        sum_of_squares += (f(A, B, nodes[i]) - np.sqrt(values[i])) ** 2
    return sum_of_squares

equations = [
    Eq(diff(phi(A, B), A), 0),
    Eq(diff(phi(A, B), B), 0)
]
sol = solve(equations)
A = sol[A]
B = sol[B]

b = 1 / B
a = b * A

print("a is", a, "and b is", b)

x_target = 1.6
value_of_x_target = hw1_A_task6_func(a, b, x_target)

print("when x is 1.6, then y is", value_of_x_target)
plt.scatter(nodes, values)
plt.scatter([x_target], [value_of_x_target])
plt.show()