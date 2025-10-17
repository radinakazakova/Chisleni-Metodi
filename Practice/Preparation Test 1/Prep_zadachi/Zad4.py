import numpy as np
import math
import sympy as sp
from sympy import symbols
import matplotlib.pyplot as plt

z, x = symbols('z, x')

def lagrange_poly(f, nodes, z):
    n = len(nodes)
    result = 0

    for k in range(n):
        Lk = 1
        for j in range(n): #namirame bazovite polinomi
            if k != j:
                Lk *= (z - nodes[j]) / (nodes[k] - nodes[j])

        result += f(nodes[k]) * Lk

    return result

def get_second_part(x_vals):
    expr = 1
    for xi in x_vals:
        expr *= (x - xi)
    return np.abs(expr)

def get_first_part(x_vals, f):
    return (np.abs(sp.diff(f, z, len(x_vals)) / math.factorial(len(x_vals))))
    
xs = np.array([0.000000001, 0.1, 0.3, 1])

lagrange = lagrange_poly(np.log, xs, z)
expand(lagrange)
