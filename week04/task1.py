'''
Задача 1

В таблицата са дадени са измервания за температурата в различни точки на нагрята метална правоъгълна пластина:
	    x = 0 	x = 2 	x = 4 	x = 6 	x = 8
y = 0 	100.00 	90.00 	80.00 	70.00 	60.00
y = 2 	85.00 	64.49 	53.50 	48.15 	50.00
y = 4 	70.00 	48.90 	38.43 	35.03 	40.00
y = 6 	55.00 	38.78 	30.39 	27.07 	30.00
y = 8 	40.00 	35.00 	30.00 	25.00 	20.00

Да се оцени температурата в точките с координати:
а) x = 4, y = 3.2;
б) x = 4.3, y = 2.7
'''

import numpy as np

from util.newton_poly import newton_poly
from util.lagrange_poly import lagrange_poly

x_nodes = [0, 2, 4, 6, 8]
y_nodes = [
    0,
    2,
    4,
    6,
    8
]

columns = [
    [100, 85, 70, 55, 40],
    [90, 64.49, 48.9, 38.78, 35],
    [80, 53.50, 38.43, 30.39, 30],
    [70, 48.15, 35.03, 27.07, 25],
    [60, 50, 40, 30, 20]
]

def get_missing_data(x_val, y_val):
    new_row_for_x_val = [(lagrange_poly(np.array(y_nodes), np.array(columns[i]), y_val)) for i in range(0, len(y_nodes))]

    return newton_poly(np.array(x_nodes), np.array(new_row_for_x_val), x_val)

print("The temperature at x = 4 and y = 3.2 is", get_missing_data(4, 3.2))
print("The temperature at x = 4.3 and y = 2.7 is", get_missing_data(4.3, 2.7))
