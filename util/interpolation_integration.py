import numpy as np

def composite_rectangles_formula(f, left, right, subintervals=100):
    nodes = np.linspace(left, right, subintervals + 1)

    return (right - left) / subintervals * sum(
        f((nodes[i-1] + nodes[i])/2)
        for i in range(1, nodes.size)
    )

def composite_trapezoids_formula(f, left, right, subintervals=100):
    nodes = np.linspace(left, right, subintervals + 1)

    return (right - left) / (2*subintervals) * sum(
        f(nodes[i-1]) + f(nodes[i])
        for i in range(1, nodes.size)
    )

def composite_simpson_formula(f, left, right, subintervals=100):
    nodes = np.linspace(left, right, subintervals + 1)

    return (right - left) / (6*subintervals) * sum(
        f(nodes[i-1]) + 4*f((nodes[i-1] + nodes[i])/2) + f(nodes[i])
        for i in range(1, nodes.size)
    )