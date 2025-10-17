import numpy as np
import math
import sympy as sp
import matplotlib.pyplot as plt


xs = np.array([0, 1.525, 3.05, 4.575, 6.1])
ys = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328])

x = sp.Symbol('x')

def lagrange_poly(nodes, values):
    n = len(nodes)
    result = 0

    for k in range(n):
        Lk = 1
        for j in range(n): #namirame bazovite polinomi
            if k != j:
                Lk *= (x - nodes[j]) / (nodes[k] - nodes[j])

        result += values[k] * Lk

    return result

polynom = sp.lambdify(x, lagrange_poly(xs, ys))
polynom(3) # 0.7423129331038849
plt.scatter(xs, ys)
x_axis = np.linspace(0, 6.1, 1000) 
plt.plot(x_axis, polynom(x_axis))
plt.show()
