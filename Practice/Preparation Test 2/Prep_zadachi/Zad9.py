from sympy import symbols, Eq, solve, diff, expand, lambdify
import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([0, 0.1, 0.2, 0.3, 0.4])
ys = np.array([1, 8, 4, 3.5, 5])
m = {0.05: 4.5, 0.15: 6, 0.25: 3.75, 0.35: 4.25}
x = sp.Symbol('x')

def lagrange_poly(nodes, values):
    n = len(nodes)
    result = 0

    for k in range(n):
        Lk = 1
        for j in range(n):
            if k != j:
                Lk *= (x - nodes[j]) / (nodes[k] - nodes[j])

        result += values[k] * Lk

    return result

polynom = sp.lambdify(x, lagrange_poly(xs, ys))

a = 0
b = 0.4
def simpson_I(f, b, a, n):
    coef = (b-a)/(6*n)
    expr = 0
    for i in range(n):
        expr += ( f(xs[i]) + 4*f((xs[i] + xs[i+1]) / 2) + f(xs[i+1]) )
    return coef * expr

n = len(xs) - 1 #колко подинтервала имаме с този брой възли
res = simpson_I(polynom, b, a, n)
res #2.033333333333329

from sympy import symbols, Eq, solve, diff, expand, lambdify
import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

#xs = np.array([0, 0.1, 0.2, 0.3, 0.4])
#ys = np.array([1, 8, 4, 3.5, 5])

a = 0
b = 0.4

def simpson_I(n, a , b, xs, ys):
    coef = (b - a) / (6*n)
    expr = 0
    for i in range(n):
        x0 = xs[i]
        x1 = xs[i+1]
        x_mid = round((x0 + x1) / 2, 1) #закръгля до 1 знак след запетаята      
        expr += ( ys[x0] + 4 * ys[x_mid] + ys[x1])
    return coef * expr

#razdelqme integrala na 2 podintegrala
# [0, 0.2] i [0.2, 0.4]
n = 1
xs1 = [0, 0.2]
ys1 = {0: 1, 0.1 :8, 0.2:4}
xs2 = [0.2, 0.4]
ys2 = {0.2:4, 0.3:3.5, 0.4:5}

integral1 = simpson_I(n, 0, 0.2, xs1, ys1)
integral2 = simpson_I(n, 0.2, 0.4, xs2, ys2)

print(integral1, integral2)
result_integral = integral1 + integral2
result_integral
