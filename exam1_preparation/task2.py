import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

from util.hermit_poly import hermit_poly

nodes = np.array([0,0,1,1,2])
values = np.array([1,0,2,6,21])

x_symbols = sp.symbols('x')
expr = hermit_poly(nodes, values, x_symbols)
print(expr)

