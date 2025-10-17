import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([3, 128, 115, 1050, 13500])

x = sp.symbols('x')
def createMatrix(vals):
    n = len(vals)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            expr = np.e ** (j * vals[i])
            row.append(expr)
        matrix.append(row)
    return np.array(matrix)

def createPolynom(coef):
    n = len(coef)
    expr = 0
    for i in range(n):
        expr += coef[i] * sp.exp(i * x)
    return expr

A = createMatrix(x_values)
coef = np.array(np.linalg.solve(A, y_values))
poly = createPolynom(coef)
poly = sp.lambdify(x, poly)
x_axis = np.linspace(1, 5, 1000)
plt.plot(x_axis, poly(x_axis))
plt.scatter(x_values, y_values)
plt.show()
