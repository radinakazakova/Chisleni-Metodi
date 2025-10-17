import numpy as np 
import matplotlib.pyplot as plt 
import math 
import sympy as sp

x_values = np.array([0, 30, 60, 90, 120, 150, 180, 240, 270, 300, 330])
y_values = np.array([45.9, 78.2, 123.5, 172.6, 223.5, 255.3, 286.0, 183.9, 116.2, 57.8, 37.7])

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

def changePeriod(t, values):
    return np.array([((2*np.pi)/t)*el for el in values])

new_x_values = changePeriod(365, x_values)
A = createTrigMatrix(new_x_values)
coef = np.array(np.linalg.solve(A, y_values))
x = sp.symbols('x')
polynom = createTrigPolynom(coef)
f = sp.lambdify(x, polynom)
f(210) # 259.9
x_axis = np.linspace(0, 6, 1000)
plt.plot(x_axis, f(x_axis))
plt.scatter(new_x_values, y_values)
plt.scatter(((2*np.pi)/365)*210, f(210), color = 'r')
plt.show()
