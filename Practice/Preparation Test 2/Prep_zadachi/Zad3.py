import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
#ln(y) = ln(a) + b*lnx
#ln(y) = c + b*X

c, b = symbols('c, b')
xs = np.array([2.5, 3.5, 5, 6, 7.5, 10, 12.5, 15, 17.5, 20])
ys = np.array([13, 11, 8.5, 8.2, 7, 6.2, 5.2, 4.8, 4.6, 4.3])

def h(X, param): # X = lnx
    b,c = param
    return b*X + c

def findPhi(h):
    expr = 0
    for i in range(len(xs)):
        expr += (h(np.log(xs[i]), (b, c)) - np.log(ys[i])) ** 2
    expand(expr)
    return expr
    
phi = findPhi(h)

sol = solve([Eq(diff(phi,b), 0),
             Eq(diff(phi,c), 0)])

def exp_func(x):
    return np.exp(float(sol[b]) * np.log(x) + float(sol[c]))

x_axis = np.linspace(2.5, 20, 100)
plt.plot(x_axis, exp_func(x_axis), 'red')
plt.scatter(xs, ys)
plt.show()
exp_func(9)
