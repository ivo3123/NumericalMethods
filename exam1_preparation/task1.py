import numpy as np
import matplotlib.pyplot as plt

from util.lagrange_poly import lagrange_poly

height = np.array([0, 1.525, 3.05, 4.575, 6.1])
density = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328])

print("Относителната плътността на въздуха на височина 3 метра е:", lagrange_poly(height, density, 3))

x_axis = np.linspace(density.min(), density.max(), 100)

plt.scatter(density, height)
plt.plot(x_axis, lagrange_poly(density, height, x_axis))
plt.xlabel('плътност')
plt.ylabel('височина')
plt.legend(['данните', 'интерполационен полином на Лагранж'])
plt.show()