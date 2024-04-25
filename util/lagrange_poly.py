import numpy as np

def get_kth_lagrange(x, kth_index, nodes):
    result = 1.0
    
    for i in range(nodes.size):
        if i != kth_index:
            result *= (x - nodes[i]) / (nodes[kth_index] - nodes[i])
    return result
    
def lagrange_poly(nodes, values, x):
    """
    Constructs an interpolating polynomial using Lagrange's method

    Args:
        nodes (np.array)
        values (np.array | function): the corresponding values of the nodes or a function does calculates them
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x)

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial at x
    """

    return sum((values(nodes[i]) if callable(values) else values[i]) * get_kth_lagrange(x, i, nodes) for i in range(nodes.size))
    