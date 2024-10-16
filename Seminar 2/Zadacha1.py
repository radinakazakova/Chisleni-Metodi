import numpy as np
import math

x0 = 0
x1 = math.pi / 6
x2 = math.pi / 3
x3 = math.pi / 2

y0 = math.sin(x0)
y1 = math.sin(x1)
y2 = math.sin(x2)
y3 = math.sin(x3)

def l03(x):
    return ((x - x1)*(x - x2)*(x - x3)) / ((x0 - x1)*(x0 - x2)*(x0 - x3))

def l13(x):
    return ((x - x0)*(x - x2)*(x - x3)) / ((x1 - x0)*(x1 - x2)*(x1 - x3))

def l23(x):
    return ((x - x0)*(x - x1)*(x - x3)) / ((x2 - x0)*(x2 - x1)*(x2 - x3))

def l33(x):
    return ((x - x0)*(x - x1)*(x - x2)) / ((x3 - x0)*(x3 - x1)*(x3 - x2))

def p(x):
    return y0*l03(x) + y1*l13(x) + y2 * l23(x) + y3 * l33(x)

result = p(math.pi / 5)
print(result)

import matplotlib.pyplot as plt

x_axis = np.linspace(0, math.pi / 2, 100)
#x_axis = np.array([x0, x1, x2, x3])
plt.plot(x_axis, np.sin(x_axis), x_axis, p(x_axis))
plt.show()
