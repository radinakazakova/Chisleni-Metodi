import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

def f(z):
    return np.log(z**3)
x = sp.symbols('x')

def div_diff(x_vals, y_vals):
    if len(x_vals) == 1:
        return m[x_vals[0]]
        
    if x_vals[0] == x_vals[-1]:
        return y_vals[-1] / math.factorial(len(x_vals) - 1)
        
    return (div_diff(x_vals[1:],y_vals[1:]) - div_diff(x_vals[:-1], y_vals[:-1])) / (x_vals[-1] - x_vals[0])

def newton_with_ermit(x_vals, y_vals):
    n = len(x_vals)
    res = 0
    for k in range(n):
        div = div_diff(x_vals[:k+1], y_vals[:k+1])
        expr = div
        for i in range(k):
            expr *= (x - x_vals[i])
        res += expr
    return res

def ermit_poly(x_vals, y_vals):
    return newton_with_ermit(x_vals, y_vals)

xs = np.array([0.2, 0.2, 0.3])
m = {0.2: f(0.2), 0.3: f(0.3)}
h = sp.log(x**3)
proizvodna1 = sp.lambdify(x, sp.diff(h, x, 1))
ys = np.array([0.2, proizvodna1(0.2), 0.3])
poly = sp.lambdify(x, ermit_poly(xs, ys))

def relative_error(x):
    return np.abs(np.abs( f(x) - poly(x)) / f(x))

x_axis = np.linspace(0.2, 0.3, 1000)
plt.plot(x_axis, relative_error(x_axis))
plt.show()
