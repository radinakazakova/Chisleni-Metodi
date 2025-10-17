import numpy as np 
import matplotlib.pyplot as plt 
import math 
import sympy as sp

x = sp.symbols('x')

def createTrigMatrix(values):
    size = len(values)
    matrix = []
    for i in range(size):
        row = []
        counter = 1
        for j in range(size):
            if j == 0:
                row.append(1)
            elif j % 2 != 0:
                row.append( np.cos(counter * values[i]) )
            else:
                row.append( np.sin(counter * values[i]) )
                counter += 1
        matrix.append(row)
    return np.array(matrix)

def createTrigPolynom(coeficient):
     size = len(coeficient)
     expr = 0
     counter = 1
     for i in range(size):
         if i == 0:
             expr += coeficient[i]
         elif i % 2 != 0: 
             expr += coeficient[i] * sp.cos(counter * x)
         else:
             expr += coeficient[i] * sp.sin(counter * x)
             counter += 1
     return expr

x_values = np.array([0, 0.95, 1.75, 4.75, 5.9])
y_values = np.array([0, 10.3, 0.5, 0.9, 1.2])
A = createTrigMatrix(x_values)
coef = np.array(np.linalg.solve(A, y_values))

polynom = createTrigPolynom(coef)
polynom = sp.lambdify(x, polynom)

x_axis = np.linspace(0, 6, 1000)
plt.plot(x_axis, polynom(x_axis))
plt.scatter(x_values, y_values)
plt.show()
