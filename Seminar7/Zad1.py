import numpy as np 
import matplotlib.pyplot as plt 
import math 
import sympy as sp

x_values = np.array([2, 5, 7, 11, 14, 16, 18, 21, 24])
y_values = np.array([7, 7.1, 7.4, 8.2, 8.9, 8.4, 7.9, 7.3, 7])

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

new_x_values = changePeriod(24, x_values)
A = createTrigMatrix(new_x_values)
coef = np.array(np.linalg.solve(A, y_values))
x = sp.symbols('x')
polynom = createTrigPolynom(coef)
f = sp.lambdify(x, polynom)
x_axis = np.linspace(0, 24, 25)
x_axis_new = np.linspace(0, 24, 1000)
plt.scatter(x_axis, f(x_axis))
plt.plot(x_axis_new, f(x_axis_new))
plt.show()

x_max = 0
fx_max = 0
currfX_max = 0
for xi in x_axis:
    currfX_max = f(xi)
    if fx_max < currfX_max:
        x_max = xi
        fx_max = currfX_max

f(x_max)
