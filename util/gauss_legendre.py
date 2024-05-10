import numpy as np
from sympy import Eq, solve, symbols, integrate

class Ith_Element:
    def __init__(self, coefficient, node):
        self.coefficient = coefficient
        self.node = node

    def __str__(self):
        return f"(node={self.node}, coefficient={self.coefficient})"
    
    def __repr__(self):
        return self.__str__()

def get_coefficients_and_nodes(nodes_count, weight_function=lambda x: 1):
    x = symbols('x')
    left = -1
    right = 1

    elements = [Ith_Element(symbols(f'A{i}'), symbols(f'x{i}')) for i in range(1, nodes_count+1)]

    algebraic_degree_of_accuracy = 2 * nodes_count - 1

    basis = lambda x, n: x ** n

    equations = [
        Eq(
            integrate(weight_function(x) * basis(x, n), (x, left, right)),
            sum(ith_elem.coefficient * ith_elem.node ** n for ith_elem in elements)
        )
        for n in range(0, algebraic_degree_of_accuracy+1)
    ]

    solutions = solve(equations)

    is_sorted = lambda arr: np.all(np.diff(arr) >= 0)

    for solution in solutions:
        nodes = [solution[symbols(f'x{i}')].evalf() for i in range(1, nodes_count+1)]
        
        if not is_sorted(nodes):
            continue

        coefficients = [solution[symbols(f'A{i}')].evalf() for i in range(1, nodes_count+1)]

        assert len(nodes) == len(coefficients), 'The count of nodes and coefficients should be the same'
        
        return (right_solution := [Ith_Element(coefficients[i], nodes[i]) for i in range(len(nodes))])

b = sum(ith_elem.coefficient * f(ith_elem.node) for ith_elem in right_solution)
print(b)

def calculate_integral(f, left=-1, right=1, nodes_count=3, weight_function=lambda x: 1):
    return (right - left) / 2 * sum(
        ith_elem.coefficient * f((right + left) / 2 + (right - left) * ith_elem.node / 2)
        for ith_elem in get_coefficients_and_nodes(nodes_count, weight_function=weight_function)
    )