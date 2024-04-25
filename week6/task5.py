'''
В таблицата са дадени данни от сигнал на акселерометър в 5 момента от време:
t, ms 	      1 	1.5   3 	4 	6
ускорение     0 	1 	  1.2 	4 	2

Да се намери обощен полином по подходящ базис, който интерполира тези данни, ако е известно, че сигналът се описва от периодична функция с период
а)
б).
Да се начертае графиката на полинома в интервала заедно с точките в една координатна система във всеки от случаите.
'''

import numpy as np
import matplotlib.pyplot as plt

from util.basis_poly import *

nodes = np.array([1, 1.5, 3, 4, 6])
values = np.array([0, 1, 1.2, 4, 2])

period1 = 2 * np.pi
period2 = 8

x_axis = np.linspace(np.min(nodes) - 4, np.max(values) + 5, 600)

period1_nodes = transform_nodes_from_period(nodes, period1)
period2_nodes = transform_nodes_from_period(nodes, period2)

plt.scatter(period1_nodes, values)
plt.scatter(period2_nodes, values)
plt.plot(x_axis, trig_poly(period1_nodes, values, x_axis))
plt.plot(x_axis, trig_poly(period2_nodes, values, x_axis))
plt.legend(['period = 2pi points', 'period = 8 points', 'period = 2pi poly', 'period = 8 poly'])
plt.show()