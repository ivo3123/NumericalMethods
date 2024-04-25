import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import sympy as sp
import math

def get_vector_column(nodes, values, basis):
    conditions = nodes.size

    matrix = np.ones([conditions, conditions])

    for row in range(conditions):
        for column in range(conditions):
            matrix[row, column] = basis(nodes[row], column)

    return np.linalg.solve(matrix, values)

def transform_nodes(nodes, A, B):
    return np.array([(A * nodes[i] + B) for i in range(nodes.size)])

def transform_nodes_from_interval(nodes, start, end):
    """
    Changes the input @nodes in the interval [@start; @end] to be in the interval [0; 2*pi].

    Args:
        nodes (np.array)
        start (float): should be a bit smaller than the smallest node
        end (float): should be a bit bigger than the largest node

    Returns:
        np.array of floats: the input @nodes in the interval [0; 2*pi].
    """

    B = start * (2 * np.pi) / (start - end)
    A = (2 * np.pi) / (end - start)

    return transform_nodes(nodes, A, B)

def transform_nodes_from_period(nodes, period):
    """
    Changes the input @nodes in the interval [0; @period] to be in the interval [0; 2*pi].
    If the input @nodes do not start from 0, consider using transform_nodes_from_interval

    Args:
        nodes (np.array)
        period: should be a bit bigger than the largest node

    Returns:
        np.array of floats: the input @nodes in the interval [0; 2*pi].
    """

    B = 0
    A = (2 * np.pi) / period

    return transform_nodes(nodes, A, B)

def basis_poly(nodes, values, x, basis):
    """
    Constructs an interpolating polynomial using a given basis.

    Args:
        nodes (np.array)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)
        basis (function(x (the x above), n (int))): a basis which defines the constructed polynomial

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """
    
    params = get_vector_column(nodes, values, basis)

    return sum(params[i] * basis(x, i) for i in range(params.size))

def trig_basis(x, n):
    return 1 if n == 0 else np.cos((n // 2 + 1) * x) if n % 2 == 1 else np.sin((n // 2) * x)

def trig_poly(nodes, values, x):
    """
    Constructs an interpolating trigonometric polynomial.
    The basis used is {1, sin(x), cos(x), ..., sin(n*x), cos(n*x)}.
    IMPORTANT: the nodes used should be in the interval [0; 2*pi].
    If they are not, then consider using transform_nodes_from_period or transform_nodes_from_interval to put them in the correct interval.

    Args:
        nodes (np.array): they must be in the interval [0; 2*pi] (look above)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    return basis_poly(nodes, values, x, trig_basis)

def exp_poly(nodes, values, x):
    """
    Constructs an interpolating exponential polynomial.
    The basis used is {1, e^x, e^(2*x), ..., e^(n*x)}

    Args:
        nodes (np.array)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    return basis_poly(nodes, values, x, lambda x, n: np.exp(x * n))

def alg_poly(nodes, values, x):
    """
    Constructs an interpolating algebraic polynomial.
    The basis used is {1, x, x^2, ..., x^n}

    Args:
        nodes (np.array)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    return basis_poly(nodes, values, x, lambda x, n : x ** n)