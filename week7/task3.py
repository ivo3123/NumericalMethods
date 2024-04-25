'''
Известно е, че връзката между скоростта на вятъра и генерираното количество електроенергия от една вятърна турбина
    може да се опише чрез кубична функция. Във файла wind_turbine_data_sample.csv се съдръжат измервания за
        количеството прозиведена електроенергия (kW) от конкретен вятърен генератор в зависимост от скоростта на вятъра (m/s).
Да се зареди файла и да се визуализират данните.
По метода на най-малките квадрати да се построи полином от трета степен, който приближава данните.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from util.mnmk import mnmk_function
from util.mnmk_matrix import mnmk_matrix_poly

file = pd.read_csv('./data/wind_turbine_data_sample.csv')

nodes = file.loc[:, 'wind speed']
values = file.loc[:, 'power output']

x_axis = np.linspace(nodes.min(), nodes.max(), 600)

plt.scatter(nodes, values)
plt.plot(x_axis, mnmk_function(nodes, values, x_axis, 4), color='red')
plt.plot(x_axis, mnmk_matrix_poly(nodes, values, x_axis, 3), color='green', linestyle='dashed')
plt.show()
