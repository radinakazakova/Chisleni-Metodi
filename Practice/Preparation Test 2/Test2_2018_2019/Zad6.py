import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

def rectangleQuadrature(f, a, b, nodes):
    n = len(nodes) - 1
    coef = (b-a)/n
    expr = 0
    for i in range(n):
        expr += f((nodes[i] + nodes[i+1])/2)
    return coef * expr
