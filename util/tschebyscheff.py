import numpy as np

def tschebyscheff(n, k, start, end):
    return ((start + end) / 2) + ((end - start) / 2) * np.cos((2*k - 1) / (2*n) * np.pi)

def get_tschebyscheff_nodes(nodes_count, start=-1, end=1):
    """
    Returns the Tschebyscheff nodes in the interval [@start; @end] used for constructing an interpolation polynomial
    The default interval in which the Tschebyscheff nodes are located is [-1, 1] but that can be ajusted with @start and @end.

    Args:
        nodes_count (int): the desired count of Tschebyscheff nodes
        start [optional] (float): [default is -1] start of the interval from which the nodes to be selected
        end [optional] (float): [default is 1] end of the interval from which the nodes to be selected

    Returns:
        np.array of floats: @nodes_count number of nodes in the interval [@start; @end]
    """
    return np.array([tschebyscheff(nodes_count, k, start, end) for k in range(0, nodes_count)])
