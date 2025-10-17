import numpy as np 
import matplotlib.pyplot as plt 
import math 
import sympy as sp

def lagrange(n, nodes, values, x):
    expr = 0
    for k in range(n):
        Lk = 1
        for i in range(n):
            if i != k:
                Lk *= (x - nodes[i]) / (nodes[k] - nodes[i])
        expr += values[k] * Lk
    return expr

def calcNodes(n, x0, h):
    x_vals = []
    for i in range(n+1):
        xi = x0 + i*h
        x_vals.append(xi)
    return np.array(x_vals)

def lagrange_poly(n, x0, h, f, x):
    nodes = calcNodes(n, x0, h)
    values = np.array(f(nodes))
    return lagrange(n+1, nodes, values, x)

#za proverka - zad 1
xs = np.array([0, 1.525, 3.05, 4.575, 6.1])
ys = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328])

x = sp.Symbol('x')

def lagrange_poly_zad1(nodes, values):
    n = len(nodes)
    result = 0

    for k in range(n):
        Lk = 1
        for j in range(n): #namirame bazovite polinomi
            if k != j:
                Lk *= (x - nodes[j]) / (nodes[k] - nodes[j])

        result += values[k] * Lk

    return result

polynom = sp.lambdify(x, lagrange_poly_zad1(xs, ys))
new_poly = sp.lambdify(x, lagrange_poly(len(xs), 0, 1.5, polynom, x))
x_axis = np.linspace(-6, 12, 1000)
plt.plot(x_axis, polynom(x_axis), x_axis, new_poly(x_axis)) #pripokrivat se izcqlo dori sled kato razshirih intervala
plt.show()
