import numpy as np
from sympy import symbols, Eq, solve, diff, expand, lambdify
import matplotlib.pyplot as plt
import math

x = symbols('x')
 
# f[x0...xn] = f[x1...xn] - f[x0..xn-1] / xn - x0 
# base: f[xi] = f(xi)
 
# xn == x0: diff(f, k, x0) / k!
 
def divided_dif(x_vals, y_vals):
    
    if len(x_vals) == 1:
        return m[x_vals[0]]
 
    if x_vals[0] == x_vals[-1]:
        return der[(x_vals[0], len(x_vals) - 1)] / math.factorial(len(x_vals)-1)
 
    
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
    polynomial_function = lambdify(x, res)
    return polynomial_function
 
x_v = np.array([0,0,1,1,1])
y_v = np.array([-1,2,0,10,40])
m = {0:-1, 1:0}
der = {(0,1): 2, (1,1): 10, (1,2):40}
newpoly = newton_poly(x_v, y_v)
x_axis = np.linspace(0, 1, 1000)
plt.plot(x_axis, newpoly(x_axis))
plt.show()
