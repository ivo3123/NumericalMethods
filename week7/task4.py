'''
Във файла amazon_sales_net_revenue.csv се съдръжат данни за годишния приход на Amazon в млрд. щатски долари за периода 2004 - 2021г.
Да се зареди файла и да се визуализират данните. По метода на най-малките квадрати, да се построи функция от вида:
f(x) = a * e ^ (b * x),
която моделира данните.
'''

import pandas as pd
import scipy.optimize as opt
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt

from util.mnmk import mnmk_function

file = pd.read_csv('./data/amazon_sales_net_revenue.csv')

nodes = file.loc[:, 'year']
values = file.loc[:, 'revenue']

def desired_func(arr, x):
    return arr[0] + arr[1] * x

def objective_function(params, f, nodes, values):
    return sum((f(params, nodes[i]) - np.log(values[i]) ** 2) for i in range(nodes.size))

def output_function(params, x):
    return np.exp(params[0] + params[1] * x)

x_axis = np.linspace(nodes.min(), nodes.max(), 600)

plt.scatter(nodes, values)
plt.plot(x_axis, mnmk_function(nodes, np.log(values), x_axis, 2, desired_kind_function=desired_func, objective_func=objective_function, output_func=output_function), color='red')
plt.show()