'''
Да се намери линейна функция, която приближава по метода на най-малките квадрати данните от таблицата:

x 	0 	1 	2 	3 	4
y 	0 	1 	1 	2 	2
'''

import scipy.optimize as opt
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import math

from util.mnmk import mnmk_function
from util.mnmk_matrix import mnmk_matrix_poly

nodes = np.array([0, 1, 2, 3, 4])
values = np.array([0, 1, 1, 2, 2])

x_axis = np.linspace(nodes.min(), nodes.max(), 100)

plt.scatter(nodes, values)
plt.plot(x_axis, mnmk_function(nodes, values, x_axis, 2), linestyle='dashed', color='purple')
plt.plot(x_axis, mnmk_matrix_poly(nodes, values, x_axis, 1))
plt.show()