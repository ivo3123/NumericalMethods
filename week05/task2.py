'''
В таблицата са дадени данни за зависимостта между нивото на алкохол в кръвта (BAC - Blood Alcohol Level) 
    и относителния риск за попадане в ПТП (т.е. колко пъти се увеличава рискът спрямо водач, който не е употребявал алкохол)
BAC 	                    0 	0.03 	0.07 	0.15 	0.21 	0.27
relative risk of crashing 	1 	1.06 	2.09 	22.1 	99.78 	328.602

Да се построи интерполационен полином по подходящ базис, който описва данните от таблицата.
Да се начертае графиката му, заедно с данните от таблицата.
'''

import numpy as np
import matplotlib.pyplot as plt

from util.basis_poly import exp_poly

nodes = np.array([0, 0.03, 0.07, 0.15, 0.21, 0.27])
values = np.array([1, 1.06, 2.09, 22.1, 99.78, 328.602])

x_axis = np.linspace(nodes.min(), nodes.max(), 400)

plt.scatter(nodes, values)
plt.plot(x_axis, exp_poly(nodes, values, x_axis))
plt.show()