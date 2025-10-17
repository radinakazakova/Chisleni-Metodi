import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import pandas as pd
#имаме y = f(x) = ax^2/b+x^2
#преобразуваме 1/y = b/a * 1/x^2 + 1/a
#полагаме А = b/a и B = 1/a
#следователно търсим А и В за: А*1/х^2 + В

xs = np.array([0.5, 0.8, 1.5, 2.5, 4])
ys = np.array([1.1, 2.4, 5.3, 7.6, 8.9])

A,B = symbols('A,B')

def f(x, param):
    A,B = param
    return A * (1/(x**2)) + B

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
    return (float(sol[A])*(1/(x**2)) + float(sol[B])) ** (-1) #превръщаме обратно със степен -1

x_axis = np.linspace(0.5, 4, 100)
plt.plot(x_axis, func(x_axis), 'red')
plt.scatter(xs, ys)
plt.show()
#
