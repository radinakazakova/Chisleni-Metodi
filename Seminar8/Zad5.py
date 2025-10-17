import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import pandas as pd
#имаме y = f(x) = ax/b+x
#преобразуваме 1/y = b/a * 1/x + 1/a
#полагаме А = b/a и B = 1/a
#следователно търсим А и В за: А*1/х + В

xs = np.array([7, 9, 15, 25, 40, 75, 100, 150])
ys = np.array([0.29, 0.37, 0.48, 0.65, 0.80, 0.97, 0.99, 1.07])

A,B = symbols('A,B')

def f(x, param):
    A,B = param
    return A * (1/x) + B

def findPhi(f):
    expr = 0
    for i in range(len(xs)):
        expr += (f(xs[i], (A, B)) - (1 / ys[i])) ** 2
    expand(expr)
    return expr
    
phi = findPhi(f)
sol = solve([Eq(diff(phi, A), 0),
             Eq(diff(phi, B), 0)])

def func(x):
    return (float(sol[A])*(1/x) + float(sol[B])) ** (-1) #превръщаме обратно със степен -1

x_axis = np.linspace(7, 150, 100)
plt.plot(x_axis, func(x_axis), 'red')
plt.scatter(xs, ys)
plt.show()
