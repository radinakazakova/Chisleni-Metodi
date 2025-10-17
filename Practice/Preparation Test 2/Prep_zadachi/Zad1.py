import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff

#y = a10^(bx) и искаме линейна функция f(x) = a + bx
#logaritmuvame s baza 10
# log(y) = log(a) + bx -> polagame log(a) = c
# log(y) = c + bx

xs = np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3])
ys = np.array([800, 975, 1500, 1950, 2900, 3600])

c, b = symbols('c, b')
def f(x, param):
    c, b = param
    return c + b*x

def findPhi(f):
    expr = 0
    for i in range(len(xs)):
        expr += (f(xs[i], (c, b)) - np.log10(ys[i])) ** 2
    expand(expr)
    return expr

phi = findPhi(f)
sol = solve([Eq(diff(phi,c), 0),
             Eq(diff(phi,b), 0)])

#10^(c + bx) -> 10^log10(a) * 10^(bx) = a * 10^(bx)
def log10_func(x):
    return np.power(10, float(sol[c]) + float(sol[b])*x)

x_axis = np.linspace(0.4, 2.3, 100)
plt.plot(x_axis, log10_func(x_axis), 'red')
plt.scatter(xs, ys)
plt.show()
