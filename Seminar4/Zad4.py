import numpy as np
import math
import sympy
import matplotlib.pyplot as plt

def f(x):
    return 1 / (1 + 25*x**2)
    
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


nodes1 = np.linspace(-1,1,11)
values1 = np.array(f(nodes1))
nodes2 = np.linspace(-1,1,5)
values2 = np.array(f(nodes2))
polynom1 = newton_poly(nodes1,values1)
polynom2 = newton_poly(nodes2, values2)
x_axis = np.linspace(-1,1, 100)
plt.plot(nodes1, polynom1(nodes1), nodes2, polynom2(nodes2), x_axis, f(x_axis))
plt.legend(['first(x)', 'second(x)', 'real(x)'])
plt.show()
