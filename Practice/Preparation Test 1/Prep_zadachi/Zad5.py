import numpy as np
import math
import sympy as sp
from sympy import symbols
import matplotlib.pyplot as plt

x = symbols('x')

def f(z):
    return np.sin(z**2) ** 3

def divided_dif_ermit(x_vals, y_vals):
    
    if len(x_vals) == 1:
        return m[x_vals[0]]
 
    if x_vals[0] == x_vals[-1]:
        return ders[(x_vals[0], len(x_vals) -1 )] / math.factorial(len(x_vals)-1) # k = len(nodes) - 1 (kato index), tursim k-ta proizvodna i k factorial
 
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
    return newton_poly_ermit(nodes, values)
    
xs = np.array([np.pi/6, np.pi/6, np.pi/5, np.pi/5, np.pi/5])
m = {np.pi/6: f(np.pi/6), np.pi/5: f(np.pi/5)}
h = sp.sin(x**2) ** 3
proizvodna1 = sp.lambdify(x, sp.diff(h, x, 1))
proizvodna2 = sp.lambdify(x, sp.diff(h, x, 2))
ders = {(np.pi/6, 1): proizvodna1(np.pi/6), (np.pi/5, 1): proizvodna1(np.pi/5), (np.pi/5, 2): proizvodna2(np.pi/5)}

ys = np.array([m[np.pi/6], proizvodna1(np.pi/6), m[np.pi/5], proizvodna1(np.pi/5), proizvodna2(np.pi/5)])

ermit_poly = ermit(xs, ys)
ermit_poly = sp.lambdify(x, ermit_poly)

x_axis = np.linspace(0, 1, 1000)
plt.plot(x_axis, ermit_poly(x_axis), x_axis, f(x_axis))
plt.scatter([np.pi/6, np.pi/5], [m[np.pi/6], m[np.pi/5]])
plt.show()
