import numpy as np

def divided_difference(nodes, values):
    curr_size = nodes.size

    if curr_size == 1:
        return values[0]
    
    return (divided_difference(nodes[1:curr_size], values[1:curr_size]) - divided_difference(nodes[0:curr_size-1], values[0:curr_size-1])) / (nodes[curr_size-1] - nodes[0])

def newton_poly(nodes, values, x):
    """
    Constructs an interpolating polynomial using Lagrange's method

    Args:
        nodes (np.array)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    curr_size = nodes.size

    result = 0.0
    result += divided_difference(nodes[0: 1], values[0: 1])
    for i in range(1, curr_size):
        product = 1.0
        for j in range(0, i):
            product *= x - nodes[j]
        
        result += divided_difference(nodes[0: i+1], values[0: i+1]) * product
    
    return result