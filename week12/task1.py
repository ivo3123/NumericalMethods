import numpy as np

def get_approximated_root_in_interval(initial_guess, max_iterations_count, function, derivatve_of_function):
    x0 = initial_guess
    last_x = x0
    for _ in range(max_iterations_count):
        next_x = last_x - (function(last_x) / derivatve_of_function(last_x))
        last_x = next_x
    
    return last_x

print(get_approximated_root_in_interval(1, 20, lambda x : x ** 3 - 2, lambda x : 3 * x ** 2))