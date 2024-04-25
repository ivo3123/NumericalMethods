'''
HW2_B.pdf
задача 8

Като се използва итеративният практически метод за приближено пресмятане на интеграли,
    описан на стр. 80 от записките и формулата на Симпсън, да се пресметне приближено стойността на интеграла:
integral from -2 to -1 ((1 - cotg(x))dx),
с грешка не по-голяма от ϵ = 10 ^ (-5).
'''

import numpy as np

epsilon = 0.00001

a = -2
b = -1

def f(x):
    ctg = np.cos(x) / np.sin(x)
    return 1 - ctg

def simpson(n):
    p = np.linspace(a, b, n + 1)  # creates n + 1 equally spaced-out points to form n subintervals
    sum = 0
    for i in range(1, n):
        sum += f(p[i-1]) + 4*f((p[i-1] + p[i]) / 2) + f(p[i])
    
    part_before_sum = (b - a) / (6 * n)

    return part_before_sum * sum

integral_value_at_n_minus_one_points = simpson(2)
integral_value_at_n_points = simpson(3)

ctr = 4

while (True):
    if abs(integral_value_at_n_minus_one_points - integral_value_at_n_points) <= epsilon:
        break
    integral_value_at_n_minus_one_points = integral_value_at_n_points
    integral_value_at_n_points = simpson(ctr)
    ctr += 1

print(integral_value_at_n_points)