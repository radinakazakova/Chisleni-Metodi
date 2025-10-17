import numpy as np
import math
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')

def lagrange_poly(nodes, values):
    n = len(nodes)
    res = 0
    for k in range(n):
        Lk = 1
        for i in range(n):
            if i != k:
                Lk *= (x - nodes[i]) / (nodes[k] - nodes[i])
        res += values[k] * Lk

    return res

lagrange_nodes = np.array([0, np.pi/4, np.pi/2])
lagrange_values = np.array(np.cos(lagrange_nodes))

poly = lagrange_poly(lagrange_nodes, lagrange_values)
lagrange = sp.lambdify(x, poly)

xs = np.array([0, 0, np.pi/2])
ys = np.array([np.cos(0), -np.sin(0), np.cos(np.pi/2)])
m = {0: np.cos(0), np.pi/2 : np.cos(np.pi/2)}
ders = {(0, 1): -np.sin(0)}

def divided_dif_ermit(x_vals, y_vals):
    
    if len(x_vals) == 1:
        return m[x_vals[0]]
 
    if x_vals[0] == x_vals[-1]:
        return ders[(x_vals[0], len(x_vals) - 1)] / math.factorial(len(x_vals)-1) # k = len(nodes) - 1 (kato index), tursim k-ta proizvodna i k factorial
 
    return (divided_dif_ermit(x_vals[1:], y_vals[1:]) - divided_dif_ermit(x_vals[:-1], y_vals[:-1])) / (x_vals[-1] - x_vals[0])
 
def newton_poly_ermit(nodes, values):
    n = len(nodes)
    res = 0
    for k in range(n):
        div = divided_dif_ermit(nodes[:k+1],values[:k+1])            
        expr = div
        for j in range(k):
            expr *= (x - nodes[j])
        
        res += expr
    return res

def ermit(nodes, values):
    return newton_poly_ermit(xs, ys)

ermit_poly = ermit(xs, ys)
ermit_poly = sp.lambdify(x, ermit_poly)

def absolute_error(node, poly):
    return np.abs( np.cos(node) - poly(node))

def relative_error(node, poly):
    return np.abs( absolute_error(node, poly) / np.cos(node) )

x_axis = np.linspace(0, 1, 1000)
plt.plot(x_axis, relative_error(x_axis, lagrange))
plt.plot(x_axis, relative_error(x_axis, ermit_poly))
plt.show()
