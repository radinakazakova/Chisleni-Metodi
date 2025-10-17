import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import sympy as sp

xs = np.array([2, 4, 6, 7, 10, 11, 14, 17, 20])
ys = np.array([4, 5, 6, 7, 8, 8, 11, 10, 12])

a,b,c,d,e,f,g = symbols('a,b,c,d, e, f,g')

def func(x, param):
    a,b,c,d, e, f,g = param
    return a + b*x + c*(x**2) + d * (x**3) + e*(x**4) + f*(x**5) + g*(x**6)

def findPhi(func):
    expr = 0
    for i in range(len(xs)):
        expr += (func(xs[i], (a,b,c,d, e,f, g)) - ys[i]) ** 2
    expand(expr)
    return expr
    
phi = findPhi(func)
sol = solve([Eq(diff(phi, a), 0),
             Eq(diff(phi, b), 0),
             Eq(diff(phi, c), 0),
             Eq(diff(phi, d), 0),
             Eq(diff(phi, e), 0),
             Eq(diff(phi, f), 0),
             Eq(diff(phi, g), 0)])

x_axis = np.linspace(2, 20, 1000)
plt.scatter(xs, ys)
plt.plot(x_axis, func(x_axis, (sol[a], sol[b], sol[c], sol[d], sol[e], sol[f], sol[g])), 'red')
plt.show()
