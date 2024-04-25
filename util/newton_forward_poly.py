import numpy as np
import math

def binomial_coefficient(t, k):
    return 1 if k == 0 else math.prod(t - i for i in range(0, k)) / math.factorial(k)

def delta(n, f, nodes):
    return sum(((-1)**(n - i)) * (binomial_coefficient(n, i) * f(nodes[i])) for i in range(0, n+1))

def newton_forward_poly(x0, h, n, f, x):
    """
    Constructs an interpolating polynomial using Newton's forward method.
    The arguments @x0, @h, @n are used to construct the nodes.
    The fist node is @x0.
    There are (@n + 1) nodes.
    Each other node is constructed by the formula: xk+1 = xk + @h,  k >= 0

    Args:
        x0 (float): the first node
        h (float): the distances between each 2 neighboring nodes
        n (float): the desired degree of the interpolated polynomial being constructed
        f (function(x (the x below))): the function to interpolate
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    t = (x - x0) / h
    nodes = [x0 + i*h for i in range(0, n+1)]
    
    return sum((delta(i, f, nodes) * binomial_coefficient(t, i)) for i in range(0, n+1))