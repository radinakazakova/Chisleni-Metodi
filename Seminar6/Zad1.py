import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp

x_values = [1,2,3,4,5]

def createMatrix(values):
    size = len(values)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append( np.e ** (j * values[i]))
        matrix.append(row)
    return np.array(matrix)

y_values = np.array([1, 12, 110, 1037, 12218])
A = createMatrix(x_values)

coef = np.array(np.linalg.solve(A, y_values))
x = sp.symbols('x')

#f = coef[0] + coef[1]*sp.exp(x) + coef[2]*sp.exp(2*x) + coef[3]*sp.exp(3*x) + coef[4]*sp.exp(4*x)
 
def createPolynom(coeficient):
     size = len(coeficient)
     expr = 0
     for i in range(size):
         expr += coeficient[i] * sp.exp(x * i)
     return expr

polynom = createPolynom(coef)
polynom
