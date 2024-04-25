'''
В таблицата са дадени данни за развитието на бактериална популация
t, h 	            1 	2 	3 	    4 	    5
бр. клетки (x1000) 	1 	12 	110 	1037 	12218

Да се намери подходяща функция, която интерполира данните.
'''

import numpy as np
import matplotlib.pyplot as plt

from util.basis_poly import exp_poly

nodes = np.array([1, 2, 3, 4, 5])
values = np.array([1, 12, 110, 1037, 12218])

x_axis = np.linspace(nodes.min(), nodes.max(), 500)

plt.scatter(nodes, values)
plt.plot(x_axis, exp_poly(nodes, values, x_axis))
plt.show()
