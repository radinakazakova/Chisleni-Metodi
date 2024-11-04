import numpy as np
import math
import sympy

x = sympy.Symbol('x')

def divided_difference(nodes,values):
    if(len(nodes) == 1):
        return values[0]
    return (divided_difference(nodes[1:], values[1:]) - divided_difference(nodes[:-1], values[:-1])) / (nodes[-1] - nodes[0])

def newton_poly(nodes, values):
    n = len(nodes)
    res = 0
    for k in range(n):
        div = divided_difference(nodes[:k+1],values[:k+1])            
        expr = div
        for j in range(k):
            expr *= (x - nodes[j])
        
        res += expr
    polynomial_function = sympy.lambdify(x, res)
    return polynomial_function

#nodes = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990]
nodes = np.arange(1920,2000,10)
values = [106.46, 123.08, 132.12, 152.27, 180.67, 205.05, 227.23, 249.46]
polynom = newton_poly(nodes, values)
res1952 = polynom(1952) #157.7280262655995
res1974 = polynom(1974) #213.5105312767937
res2000 = polynom(2000) #175.07999999999265
