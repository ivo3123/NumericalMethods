'''
Задача 6

Проведени са експерименти за определяне бързодействието на един алгоритъм за сортиране в зависимост от броя входни елементи.
Резултатите са представени в следната таблица:
Брой елементи (x1000) 	10 	      20 	   50 	    100 	 150 	  200 	   250
Време 	                0.163928  0.53282  3.00007  11.2078  26.7487  47.3297  76.8061

Да се определи приблизително колко елемента могат да се сортират за 30 сек.
'''

import numpy as np
import matplotlib as plt

from util.newton_poly import newton_poly
from util.lagrange_poly import lagrange_poly

nodes = np.array([10, 20, 50, 100, 150, 200, 250])
values = np.array([0.163928, 0.53282, 3.00007, 11.2078, 26.7487, 47.3297, 76.8061])

count = nodes.max() - nodes.min() + 1
points = np.linspace(nodes.min(), nodes.max(), count)
goal = 30

desired_x = min(points, key = lambda curr_x: abs(lagrange_poly(nodes, values, curr_x) - goal))

print('After 30 seconds the expected number of elements (x1000) is', desired_x)

'''
Initial attemp - significantly more verbose code

desired_x = 0
last_closes_result = 10000000
for i in range(0, count):
    curr_x = i + nodes.min()
    curr_y = newton_poly(nodes, values, curr_x)
    if abs(curr_y - goal) < last_closes_result:
        desired_x = curr_x
        last_closes_result = abs(curr_y - goal)
'''