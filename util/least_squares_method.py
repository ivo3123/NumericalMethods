import scipy.optimize as opt
import numpy as np

def objective_function(params, f, nodes, values):
    return sum((f(params, nodes[i]) - values[i]) ** 2  for i in range(nodes.size))

def polynomial_func(arr, x):
    degree = arr.size - 1
    return sum(arr[i] * (x ** (degree - i)) for i in range(arr.size))

def mnmk_function(nodes, values, x, vars_count, desired_kind_function=polynomial_func, objective_func=objective_function, output_func=None):
    """
    Constructs a function using the method of the smallest squares

    Args:
        nodes (np.array)
        values (np.array): the corresponding values of the nodes
        x (float | list of floats): the point, at wich the function returns the value constructed_poly(x) 
        vars_count (int): the number of variables in the @desired_kind_of_function
        desired_kind_function [optional] (function(arr (iterable of floats), x (the x above))): [default is a polynomial function] what function to manipulate the created array with size equal to @vars_count
        output_function [optional] (function(arr (iterable of floats), x (the x above))): [default is @desired_kind_function] what dunction to construct

    Returns:
        (float | list of floats): the value(s) of the constructed polynomial (defined by @output_function) at x
    """
    
    init_guess = [0 for i in range(vars_count)]
    min_res = opt.minimize(objective_function, init_guess, args = (desired_kind_function, nodes, values))
    solutions = min_res.x
    if output_func is None:
        return desired_kind_function(solutions, x)
    return output_func(solutions, x)