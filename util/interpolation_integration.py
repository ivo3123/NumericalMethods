import numpy as np

def composite_rectangles_formula(f, left, right, subintervals=100):
    """
    Calculates approximately the value of the definite integral using the Rectangles formula.

    Args:
        f (function(x)): the function under the integral
        left (float): lower bound of the integral
        right (float): upper bound of the integral
        subintervals [optional] (int): [default is 100] the number of subintervals n in the Rectangles formula, should be >= 1

    Returns:
        (float): the value of the definite integral, approximately
    """

    nodes = np.linspace(left, right, subintervals + 1)

    return (right - left) / subintervals * sum(
        f((nodes[i-1] + nodes[i])/2)
        for i in range(1, nodes.size)
    )

def composite_trapezoids_formula(f, left, right, subintervals=100):
    """
    Calculates approximately the value of the definite integral using the Trapezoids formula.

    Args:
        f (function(x)): the function under the integral
        left (float): lower bound of the integral
        right (float): upper bound of the integral
        subintervals [optional] (int): [default is 100] the number of subintervals n in the Trapezoids formula, should be >= 1

    Returns:
        (float): the value of the definite integral, approximately
    """

    nodes = np.linspace(left, right, subintervals + 1)

    return (right - left) / (2*subintervals) * sum(
        f(nodes[i-1]) + f(nodes[i])
        for i in range(1, nodes.size)
    )

def composite_simpson_formula(f, left, right, subintervals=100):
    """
    Calculates approximately the value of the definite integral using the Simpson's formula.

    Args:
        f (function(x)): the function under the integral
        left (float): lower bound of the integral
        right (float): upper bound of the integral
        subintervals [optional] (int): [default is 100] the number of subintervals n in the Simpson's formula, should be >= 1

    Returns:
        (float): the value of the definite integral, approximately
    """

    nodes = np.linspace(left, right, subintervals + 1)

    return (right - left) / (6*subintervals) * sum(
        f(nodes[i-1]) + 4*f((nodes[i-1] + nodes[i])/2) + f(nodes[i])
        for i in range(1, nodes.size)
    )