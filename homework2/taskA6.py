'''
HW2_A.pdf
задача 6

Намерете приближено
integral from 0 to pi (f(x)dx),
използвайки съставната квадратурна формула на Симпсън, като са известни само следните стойности на функцията:

x       0         pi/4      pi/2      3*pi/4    pi
f(x)    1.0000    0.3431    0.2500    0.3431    1.0000
'''

import numpy as np

nodes = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
values = np.array([1, 0.3431, 0.25, 0.3431, 1])

a = 0
b = np.pi

i = 2
n = nodes.size // 2
print(n)

sum = 0
while (i <= nodes.size):
    sum += values[i-2] + 4*values[i-1] + values[i]
    i += 2

part_before_sum = (b - a) / (6 * n)

integral_value = part_before_sum * sum

print(integral_value)