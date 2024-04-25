'''
Във файла CO_2_data.csv се съдръжат данни за нивата на въглеродния диоксид в атмосферата (в млрд. тонове) за периода 1940-2022г.
Да се зареди файла и да се визуализират данните.
По метода на най-малките квадрати да се построи линейна функция, която приближава данните.
'''

import pandas as pd
import scipy.optimize as opt
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt

from util.mnmk import mnmk_function
from util.mnmk_matrix import mnmk_matrix_poly

file = pd.read_csv('./data/CO_2_data.csv')

nodes = file.loc[:, 'year']
values = file.loc[:, 'co2']

x_axis = np.linspace(nodes.min(), nodes.max(), 300)

plt.scatter(nodes, values)
plt.plot(x_axis, mnmk_function(nodes, values, x_axis, 2), color='red')
plt.plot(x_axis, mnmk_matrix_poly(nodes, values, x_axis, 1), color='green', linestyle='dashed')
plt.show()
