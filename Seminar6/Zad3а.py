import numpy as np 
import matplotlib.pyplot as plt 
import math 
import sympy as sp

x_values = [1, 1.5, 3, 4, 6]

def createTrigMatrix(values):
    size = len(values)
    matrix = []
    for i in range(size):
        row = []
        counter = 1
        for j in range(size):
            if j == 0:
                row.append(1)
            elif j% 2 != 0:
                row.append( np.cos(counter * values[i]) )
            else:
                row.append( np.sin(counter * values[i]) )
                counter += 1
        matrix.append(row)
    return np.array(matrix)
            
A = createTrigMatrix(x_values)
y_values = np.array([0, 1, 1.2, 4, 2])
coef = np.array(np.linalg.solve(A, y_values))
x = sp.symbols('x')

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

polynom = createTrigPolynom(coef)
f = sp.lambdify(x, polynom)
x_axis = np.linspace(0, 4 * np.pi, 1000)
plt.scatter(x_values, y_values)
plt.plot(x_axis, f(x_axis))
plt.show()

def changePeriod(t, values):
    return np.array([((2*np.pi)/t)*el for el in values])

new_x_values = changePeriod(8, x_values)
A2 = createTrigMatrix(new_x_values)
coef2 = np.array(np.linalg.solve(A2, y_values))
polynom2 = createTrigPolynom(coef2)
f2 = sp.lambdify(x, polynom2)
plt.scatter(new_x_values, y_values)
plt.plot(x_axis, f2(x_axis))
plt.show()
    
