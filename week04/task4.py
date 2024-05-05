'''
Задача 4

Определете стойността 𝑐𝑜𝑠52∘, 
    като построите интерполационния полином на Лагранж 
        за функцията 𝑐𝑜𝑠𝑥 с възли 45∘,50∘,55∘,60∘ по формулата на Нютон за интерполиране напред.
'''

import numpy as np

from util.newton_forward_poly import newton_forward_poly
from util.lagrange_poly import lagrange_poly

print('Value at 52deg from newton_poly:', newton_forward_poly(45, 5, 4, np.cos, 52))
print('Value at 52deg from lagrange_poly:', lagrange_poly(np.array([45, 50, 55, 60]), np.cos, 52))
print('Actual value at 52deg:', np.cos(np.deg2rad(52)))