'''
Define a function Lagrange(n, A, B, f, x) that constructs the Lagrange interpolation polynomial of degree n for the function f(x),
    using equidistant nodes in the interval [A, B], using the Lagrange formula.
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
