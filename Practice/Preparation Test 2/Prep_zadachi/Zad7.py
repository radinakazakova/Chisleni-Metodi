from sympy import symbols, Eq, solve, diff, expand, lambdify, integrate
import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(np.sin(x)) - 2 * x**2

def calc_res(A1, A2, A3, x1, x2, x3):
    return A1 * phi(float(x1)) + A2 * phi(float(x2)) + A3 * phi(float(x3))
a = 0
b = 1

def phi(x):
    return (b-a)/2 * f((b+a)/2 + ((b-a)/2) * x)

x, A1, A2, A3, x1, x2, x3 = symbols('z, A1, A2, A3, x1, x2, x3')

sol = solve([Eq( A1 + A2 + A3, integrate(1, (x, -1, 1))),
             Eq( A1*x1 + A2*x2 + A3*x3, integrate(x, (x, -1, 1))),
             Eq( A1*(x1**2) + A2*(x2**2) + A3*(x3**2), integrate(x**2, (x, -1, 1))),
             Eq( A1*(x1**3) + A2*(x2**3) + A3*(x3**3), integrate(x**3, (x, -1, 1))),
             Eq( A1*(x1**4) + A2*(x2**4) + A3*(x3**4), integrate(x**4, (x, -1, 1))),
             Eq( A1 * x1**5 + A2*(x2**5) + A3*(x3**5), integrate(x**5, (x, -1, 1)))])
coef = sol[0]
res = calc_res(coef[A1], coef[A2], coef[A3], coef[x1],coef[x2], coef[x3])
res
