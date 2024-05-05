'''
Задача 5

Известно е (вж. лекции), че най-добрите възли за интерполация в интервала [−1,1] 
    са т.нар. Чебишови възли, които се задават по формула.
Да се построи интерполационен полином от 10-та степен за функцията на Рунге,
    като за целта се използват съответните Чебишови възли в интервала [−1,1]
Да се построи графика на абсолютната грешка.
'''

import matplotlib.pyplot as plt
import numpy as np

from util.newton_poly import newton_poly
from util.tschebyscheff import get_tschebyscheff_nodes

def runge(x):
    return 1 / (1 + 25 * (x ** 2))

def get_abs_error(x, real_function, nodes, values):
    return abs(real_function(x) - newton_poly(nodes, values, x))

nodes_degree_10 = get_tschebyscheff_nodes(degree := 10)
values_degree_10 = runge(nodes_degree_10)

x_axis = np.linspace(-1, 1, 1000)

plt.plot(x_axis, newton_poly(nodes_degree_10, values_degree_10, x_axis), label='deg_10', color='blue')
plt.plot(x_axis, runge(x_axis), label='runge', linestyle='dashed', color='orange')
plt.legend(['deg_10', 'runge'])
plt.show()

plt.plot(x_axis, get_abs_error(x_axis, runge, nodes_degree_10, values_degree_10), color='red')
plt.legend(['abs_error'])
plt.show()