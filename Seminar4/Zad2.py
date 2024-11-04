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
    return sympy.simplify(res) #ne mojem da izpolzwame kato funkciq, resultata e samo chisla i simvoli
  #reshenine :     polynomial_function = sympy.lambdify(x, res)
                   #return polynomial_function

'''
#за проверка
nodes = [0, 1]
expr = 1 / (1 + x)
f = sympy.lambdify(x, expr)
values = f(np.array(nodes))

poly = newton_poly(nodes, values)
poly
'''
