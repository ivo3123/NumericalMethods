import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import Eq, solve, symbols, integrate

def gaus_luijander(nodesCount, weight_function, lower_bound, upper_bound):
    if nodesCount < 2 or nodesCount > 3:
        raise ValueError('The function only works when nodesCount is 2 or 3')

    if nodesCount == 2:
        A1, x1, A2, x2, x = symbols('A1, x1, A2, x2, x')
    
        equations = [
            Eq(integrate(weight_function(x) * 1, (x, lower_bound, upper_bound)), A1 + A2),
            Eq(integrate(weight_function(x) * x, (x, lower_bound, upper_bound)), A1 * x1 + A2 * x2),
            Eq(integrate(weight_function(x) * x ** 2, (x, lower_bound, upper_bound)), A1 * x1 ** 2 + A2 * x2 ** 2),
            Eq(integrate(weight_function(x) * x ** 3, (x, lower_bound, upper_bound)), A1 * x1 ** 3 + A2 * x2 ** 3)
        ]

        sol = solve(equations, dict= True)

        for i in range(len(sol)):
            if sol[i][x1] < sol[i][x2]:
                return [(sol[i][A1], sol[i][x1].evalf()), (sol[i][A2], sol[i][x2])]

    if nodesCount == 3:
        A1, x1, A2, x2, A3, x3, x = symbols('A1, x1, A2, x2, A3, x3, x')
    
        equations = [
            Eq(integrate(weight_function(x) * 1, (x, lower_bound, upper_bound)), A1 + A2 + A3),
            Eq(integrate(weight_function(x) * x, (x, lower_bound, upper_bound)), A1 * x1 + A2 * x2 + A3 * x3),
            Eq(integrate(weight_function(x) * x ** 2, (x, lower_bound, upper_bound)), A1 * x1 ** 2 + A2 * x2 ** 2 + A3 * x3 ** 2),
            Eq(integrate(weight_function(x) * x ** 3, (x, lower_bound, upper_bound)), A1 * x1 ** 3 + A2 * x2 ** 3 + A3 * x3 ** 3),
            Eq(integrate(weight_function(x) * x ** 4, (x, lower_bound, upper_bound)), A1 * x1 ** 4 + A2 * x2 ** 4 + A3 * x3 ** 4),
            Eq(integrate(weight_function(x) * x ** 5, (x, lower_bound, upper_bound)), A1 * x1 ** 5 + A2 * x2 ** 5 + A3 * x3 ** 5)
        ]

        sol = solve(equations, dict= True)

        for i in range(len(sol)):
            if sol[i][x1] < sol[i][x2] and sol[i][x1] < sol[i][x3] and sol[i][x2] < sol[i][x3]:
                return [(sol[i][A1], sol[i][x1]), (sol[i][A2], sol[i][x2]), (sol[i][A3], sol[i][x3])]

def get_value(nodesCount, actualFunction, weight_function = lambda x : 1, lower_bound = -1, upper_bound = 1):
    sol = gaus_luijander(nodesCount, weight_function, lower_bound, upper_bound)

    return sum(sol[i][0] * actualFunction(sol[i][1]) for i in range(len(sol)))

def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

def phi(t):
    return f(0.4 * t + 0.4)

print(get_value(3, lambda x : x + 1))
print(get_value(2, phi))
