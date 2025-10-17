import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import sympy as sp
import scipy

a = np.pi/4
b = np.pi/2
z = sp.symbols('z')
n = symbols('n', positive=True)
x_axis = np.linspace(1, 2, 1000)
#грешка не по-голяма от 10^-5
threshold = 10 ** (-5)

def f(x):
    return np.cos(x) * np.sin(2*x)
    
h = sp.cos(z) * sp.sin(2*z)

def derivativeMax(f, z, num):
    poly = sp.lambdify(z, sp.Abs(sp.diff(f, z, num)))
    return max(poly(x_axis))

def simpson_error_estimate(f, z, b, a, n):
    maxDer = derivativeMax(f, z, 4)
    return (maxDer /(2880 * (n**4))) * ((b-a)**5)

error_poly = simpson_error_estimate(h, z, b, a, n)
equation = Eq(error_poly, threshold)
sol = solve(equation, n)
integer_N = int(np.ceil(sol[0]))
print("n =", integer_N)
def simpson_I(f, b, a, n):
    coef = (b-a)/(6*n)
    expr = 0
    x_nodes = np.linspace(a, b, n+1)
    for i in range(n):
        expr += ( f(x_nodes[i]) + 4*f( (x_nodes[i] + x_nodes[i+1]) / 2) + f(x_nodes[i+1]) )
    return coef * expr

simp_res = simpson_I(f, b, a, integer_N)
print("Simpson",simp_res)
res, error = scipy.integrate.quad(f,a,b)
print("Exact value", res)
