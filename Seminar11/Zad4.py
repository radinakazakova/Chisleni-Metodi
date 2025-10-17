import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, integrate
import sympy as sp

x, A1, A2, A3, x1, x2, x3 = symbols('x, A1, A2, A3, x1, x2, x3')
a = 0
b = 1

def f(x_):
    return np.sin(2 * x_)

equations = [Eq(A1 + A2 + A3, integrate(1, (x, 0, 1))), 
            Eq(A1 * x1 + A2 * x2 + A3 * x3, integrate(x, (x, 0, 1))),
            Eq(A1 * x1 ** 2 + A2 * x2 ** 2 + A3 * x3 ** 2, integrate(x ** 2, (x, 0, 1))),
            Eq(A1 * x1 ** 3 + A2 * x2 ** 3 + A3 * x3 ** 3, integrate(x ** 3, (x, 0, 1))),
            Eq(A1 * x1 ** 4 + A2 * x2 ** 4 + A3 * x3 ** 4, integrate(x ** 4, (x, 0, 1))),
            Eq(A1 * x1 ** 5 + A2 * x2 ** 5 + A3 * x3 ** 5, integrate(x ** 5, (x, 0, 1)))]

sol = solve(equations, A1, x1, A2, x2, A3, x3, dict = True)
coef = sol[0]
res = coef[A1] * f(float(coef[x1])) + coef[A2] * f(float(coef[x2])) + coef[A3] * f(float(coef[x3]))
res
