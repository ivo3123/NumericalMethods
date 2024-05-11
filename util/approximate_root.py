import numpy as np

def newton_raphson(initial_guess, f, f_der, epsilon=0.00001, max_intervals=100_000):
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