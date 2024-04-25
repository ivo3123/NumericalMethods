'''
В таблицата са дадени данни за средните месечни количества слънчева радиация на територията на България, като лиспват данни за м. август

t, месец 	       Я 	    Ф 	    М 	    А 	    М 	    Ю 	    Ю 	     A 	  С 	    O 	    Н 	    Д
слънчева радиация  45.9 	78.2 	123.5 	172.6 	223.5 	255.3 	286.0 		  183.9 	116.2 	57.8 	37.7

Данните са осреднени на 30 дни, т.е. можем да считаме, че разстоянието между измерванията в два съседни месеца е 30. Като се има предвид това,
    както и факта, че разглежданият процес е с период 365 дни, да се намери обобщен полином по подходящ базис,
            който описва данните в таблицата.
Като се използва така намерения полином, да се пресметне приближено количеството слънчева радиация, съответстващо на м. август.
Да се сравни с действителната стойност - 257.9.
'''
import numpy as np
import matplotlib.pyplot as plt

from util.basis_poly import *
from util.lagrange_poly import lagrange_poly

nodes = np.array([15.0, 45, 75, 105, 135, 165, 195, 255, 285, 315, 345])
values = np.array([45.9, 78.2, 123.5, 172.6, 223.5, 255.3, 286.0, 183.9, 116.2, 57.8, 37.7])

nodes = transform_nodes_from_period(nodes, 365)

august = 225
missing_x = 2 * np.pi * august / 365
missing_x_value = trig_poly(nodes, values, missing_x)
real_value = 257.9
error = abs(real_value - missing_x_value)
print('Radiation in august')
print('Estimate value:', missing_x_value)
print('Real value:', real_value)
print('Error of estimation:', error)

x_axis = np.linspace(nodes.min(), nodes.max() + 6, 200)

plt.scatter(nodes, values)
plt.scatter(missing_x, real_value)
plt.plot(x_axis, trig_poly(nodes, values, x_axis))
plt.legend(['radiation per month', 'August radiation', 'trig poly'])
plt.show()

