import numpy as np

def newton_raphson(initial_guess, f, f_der, epsilon=0.00001, max_intervals=100_000):
    """
    Solve the equation @f(x) = 0 approximately using the Newton-Raphson method

    Args:
        initial_guess (float): should be somewhat 'close' to the desired root; information about the root beforehand is required
        f (function(x)): a function for which we want to solve f(x) = 0
        f_der (function(x)): the derivative of @f
        epsilon [optional] (float): [default is 0.00001] the precision with whcih to solve the equation @f(x) = 0, should be 'small'
        max_intervals [optional] (int): [default is 100_000] the maximum number of iterations before the method is over

    Returns:
        (float, list of floats): an approximated solution x from the equation @f(x) = 0 and the approximation in each iteration
    """

    x0 = initial_guess

    xn = x0
    iterations = 0

    iterations = []

    while True:
        assert f_der(xn) != 0, f'f({xn}) in denominator is zero'

        xn_plus_1 = xn - f(xn)/f_der(xn)

        iterations.append(xn_plus_1)

        if abs(xn_plus_1 - xn) < epsilon:
            return xn_plus_1, iterations

        xn = xn_plus_1

def bisection(start, end, f, epsilon=0.00001, max_intervals=100_000):
    """
    Solve the equation @f(x) = 0 approximately using the Bisection method
    Important!: @f(@start) * @f(@end) should be < 0

    Args:
        start, end (float, float): start < end and the desired root should be in the interval (start, end); information about the root beforehand is required
        f (function(x)): a function for which we want to solve f(x) = 0
        epsilon [optional] (float): [default is 0.00001] the precision with whcih to solve the equation @f(x) = 0, should be 'small'
        max_intervals [optional] (int): [default is 100_000] the maximum number of iterations before the method is over

    Returns:
        (float, list of floats): an approximated solution x from the equation @f(x) = 0 and the approximation in each iteration
    """

    assert f(start) * f(end) < 0, f'f({start}) * f({end}) should be < 0'

    iterations = []

    get_mid = lambda left, right: (right - left) / 2 + left

    while (end - start) >= epsilon:
        mid = get_mid(start, end)

        if f(mid) < 0:
            start = mid
        else:
            end = mid
        
        iterations.append((start, end))
    
    return get_mid(start, end) , iterations