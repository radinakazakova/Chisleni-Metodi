import numpy as np
import sympy as sp
import math
x = sp.symbols('x')
def divided_dif(x_vals, y_vals):
    key = tuple(x_vals)
    if key in rr:
        return rr[key]
    
    if len(x_vals) == 1:
        rr[key] = y_vals[0]
        return y_vals[0]
    rr[key] =  (divided_dif(x_vals[1:], y_vals[1:]) - divided_dif(x_vals[:-1], y_vals[:-1])) / (x_vals[-1] - x_vals[0])
    return rr[key]
 
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

rr = {}
newton_poly([0,1,2,4], [1,1,2,2])
print(rr)
