import numpy as np
import numpy.linalg

def least_squares_method_matrix_function(nodes, values, degree):
    points_count = nodes.size
    n = degree + 1

    values_vector_column = np.array([sum(values[i] * (nodes[i] ** s) for i in range(points_count)) for s in range(n)])

    matrix = np.ones([n, n])
    for row in range(n):
        for column in range(n):
            matrix[row, column] = sum(nodes[i] ** (row + column) for i in range(points_count))

    return np.linalg.solve(matrix, values_vector_column)

def least_squares_method_matrix_poly(nodes, values, x, degree):
    """
    Constructs a polynomial using the method of the smallest squares in its matrix form

    Args:
        nodes (np.array)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x) 
        degree (int): the desired degree of the constructed polynomial

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    coefficients = least_squares_method_matrix_function(nodes, values, degree)
    return sum(coefficients[i] * x ** i for i in range(coefficients.size))