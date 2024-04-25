import numpy as np

def tschebyscheff(degree, k, start, end):
    return ((start + end) / 2) + ((end - start) / 2) * np.cos((2*k - 1) / (2*degree) * np.pi)

def get_tschebyscheff_nodes(degree, start=-1, end=1):
    """
    Returns the Tschebyscheff nodes in the interval [@start; @end] used for constructing an interpolating polynomial
    Note that we need (n + 1) nodes to construct a polynomial of degree n, but we only need n Tschebyscheff nodes to to construct a polynomial of degree n.
    The default interval in which the Tschebyscheff nodes are located is [-1, 1] but that can be ajusted with @start and @end.

    Args:
        degree (int): the desired degree of the interpolated polynomial
        start [optional] (float): [default is -1] start of the interval from which the nodes to be selected
        end [optional] (float): [default is 1] end of the interval from which the nodes to be selected

    Returns:
        np.array of floats: @degree number of nodes in the interval [@start; @end]
    """
    return np.array([tschebyscheff(degree, k, start, end) for k in range(1, degree+1)])