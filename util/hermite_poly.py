import numpy as np
import math

def get_derivative(nodes, values, left, right):
    for i in range(nodes.size):
        if nodes[i] == nodes[left]:
            return values[i + right - left]
    return None

def divided_difference_generalized(nodes, values, left, right):
    if nodes[left] == nodes[right]:
        return get_derivative(nodes, values, left, right) / math.factorial(right - left)
    else:
        return (divided_difference_generalized(nodes, values, left+1, right) - divided_difference_generalized(nodes, values, left, right-1)) / (nodes[right] - nodes[left])

def hermite_poly(nodes, values, x):
    """
    Constructs an interpolating polynomial using Hermit's method.
    It's acceptable that 2 different nodes have the same value.
    For that case we use the appropriate derivative as the corresponding value.
    It's important that the values are correct, else the function would not return a reasonable value.

    Args:
        nodes (np.array)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    return sum(divided_difference_generalized(nodes, values, 0, i) * (math.prod(x - nodes[j] for j in range(0, i))) for i in range(nodes.size))
