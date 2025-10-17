from sympy import symbols, Eq, solve, diff, expand, lambdify
import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

a = -1
b = 1

def f(x):
    return (-(x ** 4) + 1)

def trapezoid_I(f, b, a, n):
    coef = (b-a)/(2*n)
    x_nodes = np.linspace(a, b, n+1)
    expr = 0
    for i in range(n):
        expr += (f(x_nodes[i]) + f(x_nodes[i+1]))
    return coef * expr

res = trapezoid_I(f, b, a, 4)
res
