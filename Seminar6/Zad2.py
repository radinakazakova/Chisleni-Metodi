import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp


x_values = [0, 0.03, 0.07, 0.15, 0.21, 0.27]

def createMatrix(values):
    size = len(values)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append( np.e ** (j * values[i]))
        matrix.append(row)
    return np.array(matrix)

A = createMatrix(x_values)
y_values = np.array([1, 1.06, 2.09, 22.1, 99.78, 328.602])
coef = np.array(np.linalg.solve(A, y_values))
x = sp.symbols('x')

#f = coef[0] + coef[1]*sp.exp(x) + coef[2]*sp.exp(2*x) + coef[3]*sp.exp(3*x) + coef[4]*sp.exp(4*x) + coef[5] * sp.exp(5*x)
def createPolynom(coeficient):
     size = len(coeficient)
     expr = 0
     for i in range(size):
         expr += coeficient[i] * sp.exp(x * i)
     return expr

polynom = createPolynom(coef)
f = sp.lambdify(x, polynom)
f(0) # okolo 1
f(0.27) #smqta pravilno
