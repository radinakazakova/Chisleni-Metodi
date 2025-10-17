import numpy as np 
import matplotlib.pyplot as plt 
import math 
import sympy as sp

x = sp.symbols('x')
xs = np.array([0, 2, 4, 6, 8])
ys = np.array([0.1, 0.009, 0.0011, 0.00003, 0.0000012])

def createMatrix(values):
    size = len(values)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append( 1 / ((j+1) + values[i]))
        matrix.append(row)
    return np.array(matrix)

def createPolynom(coeficient):
     size = len(coeficient)
     expr = 0
     for i in range(size):
         expr += coeficient[i] * (1/ ((i+1) + x))
     return expr

A = createMatrix(xs)
coef = np.array(np.linalg.solve(A, ys))
polynom = createPolynom(coef)
polynom = sp.lambdify(x, polynom)

x_axis = np.linspace(0, 8, 10000)
plt.plot(x_axis, polynom(x_axis))
plt.scatter(xs, ys)
plt.show()
