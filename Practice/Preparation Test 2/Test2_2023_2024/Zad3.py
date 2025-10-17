import numpy as np
import sympy as sp
import scipy
import matplotlib.pyplot as plt

a = 1
b = 3
threshold = 10 **(-5)
n = sp.symbols('n', positive = True)

def f(x):
    return np.sin(x)**2

maxDerivative = 8

def error_simpson(f):
    return (((b-a)**5)/(2880 * (n**4)) * maxDerivative)

errorPoly = error_simpson(f)
equation = sp.Eq(errorPoly, threshold)
N = int(np.ceil(sp.solve(equation, n)))
print(N)
def simpson_I(f, N):
    coef = (b-a) /(6*N)
    expr = 0
    x_nodes = np.linspace(a, b, N+1)
    for i in range(N):
        expr += (f(x_nodes[i]) + 4 * f((x_nodes[i] + x_nodes[i+1])/2) + f(x_nodes[i+1]))
    return coef * expr

res = simpson_I(f, N)
res #1.297180885472451
res1, error1 = scipy.integrate.quad(f, a, b)
res1 #1.2971782312561517
