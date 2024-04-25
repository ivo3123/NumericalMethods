'''
Дадени са данни за усвояването на лекарство от организма.
В таблицата е дадена концентрацията на лекарството в кръвта, като функция на времето:

t, h 	                    0 	    2 	    4 	    6 	        8
концентрация (в промили) 	0.1 	0.009 	0.0011 	0.00003 	0.0000012

Да се намери обобщен полином, който интерполира данните. За целта да се избере подходящ базис измежду следните:
{1, e^x, e^(2*x), ..., e^(n*x)}
{1 / (1 + x), 1 / (2 + x), ..., 1 / (n + x)}
{1, e^(-x), e^(-2*x), ..., e^(-n*x)}
{1 / (1 - x), 1 / (2 - x), ..., 1 / (n - x)}

Обосонвете избора си, като обясните кой от изброените базиси е подходящ и защо останалите не са.
'''

import numpy as np
import matplotlib.pyplot as plt

from util.basis_poly import *

nodes = np.array([0, 2, 4, 6, 8])
values = np.array([0.1, 0.009, 0.0011, 0.00003, 0.0000012])

x_axis = np.linspace(nodes.min(), nodes.max(), 100)

basis1 = lambda x, n: np.e ** (n * x)
basis2 = lambda x, n: 1 / (1 + n + x)
basis3 = lambda x, n: np.e ** (-n * x)
basis4 = lambda x, n: 1 / (1 + n - x)

plt.scatter(nodes, values)
plt.plot(x_axis, basis_poly(nodes, values, x_axis, basis1))
plt.show()

plt.scatter(nodes, values)
plt.plot(x_axis, basis_poly(nodes, values, x_axis, basis2))
plt.show()

plt.scatter(nodes, values)
plt.plot(x_axis, basis_poly(nodes, values, x_axis, basis3))
plt.show()

'''
Ясно се вижда, че първият и третият базис не са подходящи
Четвъртият базис допуска стойност 0 в знаменателя и съответно не е подходящ.

Вторият базис описва поведението на данните добре и съответно е подходящ.
'''