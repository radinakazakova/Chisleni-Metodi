#1 към 1 със задача 4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
#y = a * x * e^(b*x)
#lny = lna + lnx + bx
# c = lna

xs = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.5, 1.7, 1.8])
ys = np.array([0.75, 1.25, 1.45, 1.25, 0.83, 0.55, 0.35, 0.28, 0.18])

c, b = symbols('c b')

def f(ln_x, x, param):
    c, b = param
    return c + ln_x + b*x

def findPhi(f):
    expr = 0
    for i in range(len(xs)):
        expr += (f(np.log(xs[i]), xs[i], (c,b)) - np.log(ys[i])) ** 2
    expand(expr)
    return expr
    
phi = findPhi(f)

sol = solve([Eq(diff(phi,b), 0),
             Eq(diff(phi,c), 0)])

# c + ln_x + bx
#e^(c + ln_x + bx) = e^c * e^ln_x * e^bx = a * x * e^bx
def exp_func(x):
    return np.exp(float(sol[c]) + np.log(x) + float(sol[b]) * x)

x_axis = np.linspace(0.1, 1.8, 100)
plt.scatter(xs, ys)
plt.plot(x_axis, exp_func(x_axis), 'red')
plt.show()
