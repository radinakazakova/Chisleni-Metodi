import numpy as np
import sympy as sp
import math

x = sp.Symbol('x')

def divided_dif(x_vals, y_vals):
    
    if len(x_vals) == 1:
        return m[x_vals[0]]
 
    if x_vals[0] == x_vals[-1]:
        return ders[(x_vals[0], len(x_vals) - 1)] / math.factorial(len(x_vals)-1) # k = len(nodes) - 1 (kato index), tursim k-ta proizvodna i k factorial
 
    
    return (divided_dif(x_vals[1:], y_vals[1:]) - divided_dif(x_vals[:-1], y_vals[:-1])) / (x_vals[-1] - x_vals[0])
 
def newton_poly(nodes, values):
    n = len(nodes)
    res = 0
    for k in range(n):
        div = divided_dif(nodes[:k+1],values[:k+1])            
        expr = div
        for j in range(k):
            expr *= (x - nodes[j])
        
        res += expr
    return res

xs = np.array([0, 0, 1, 1, 2])
ys = np.array([1, 0, 2, 6, 21])
m = {0: 1, 1:2, 2:21}
ders = {(0, 1): 0, (1, 1): 6}

polynom = newton_poly(xs, ys)
sp.expand(polynom)
