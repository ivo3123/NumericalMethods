'''
Given Points: We start with at least four fixed points, as well as a target point (x0, y0).

Constructing Polynomials: For each combination of three fixed points,
    we construct an interpolated polynomial using methods such as Lagrange interpolation or polynomial regression.
This polynomial represents the relationship between the selected three points.

Sorting Polynomials: After constructing all possible polynomials,
    we need to sort them based on their proximity to the target point (x0, y0).
We measure this proximity by calculating the absolute difference between the value of each polynomial
    at the target x-coordinate (Pi(x0)) and the y-coordinate of the target point (y0).
We want to minimize this absolute difference.
'''

import numpy as np
import matplotlib.pyplot as plt

from util.lagrange_poly import lagrange_poly

DESIRED_DEGREE = 3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [
    Point(-3, 12.2),
    Point(-14, 8.2),
    Point(1.1, -1.3),
    Point(5.22, -10),
    Point(9, -6)
]

target_point = Point(0, 0)

def get_all_points_indexes_combinations(count, desired_degree=DESIRED_DEGREE, result=[]):
    if count == desired_degree:
        result.append([i for i in range(desired_degree-1, -1, -1)])
        return result

    for i in range(count-2, 0, -1):
        for j in range(i-1, -1, -1):
            if(i != j):
                result.append([count-1, i, j])

    return get_all_points_indexes_combinations(count-1, desired_degree, result)


def sort_polinoms_by_proximity_to_target(points, desired_degree=DESIRED_DEGREE):
    combinations = get_all_points_indexes_combinations(len(points))
    disered_combinations_order = sorted(
        combinations,
        key = lambda l: abs(
            lagrange_poly(np.array([points[i].x for i in l]), np.array([points[i].y for i in l]), target_point.x) - target_point.y
        )
    )
    return disered_combinations_order


def construct_closest_poly(points, target_point, desired_degree=DESIRED_DEGREE):
    min_of_points = min(points, key = lambda p: p.x)
    lower_bound = min(min_of_points.x, target_point.x) - 1

    max_of_points = max(points, key = lambda p: p.x)
    upper_bound = max(max_of_points.x, target_point.x) + 1

    combinations = sort_polinoms_by_proximity_to_target(points)

    x_axis = np.linspace(lower_bound, upper_bound, 1000)
    for i in range(0, len(combinations)):
        xs = [points[j].x for j in combinations[i]]
        ys = [points[j].y for j in combinations[i]]

        diff = abs(lagrange_poly(np.array(xs), np.array(ys), target_point.x) - target_point.y)

        plt.plot(x_axis, lagrange_poly(np.array(xs), np.array(ys), x_axis))
        plt.scatter([target_point.x], [target_point.y], color='red')
        plt.scatter(xs, ys, color='blue')
        plt.title(f'Diff is {round(diff, 2)}')
        plt.show()


construct_closest_poly(points, target_point)
