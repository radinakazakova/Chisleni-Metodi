# Initial try for solution (incorrect)
import numpy as np
import math
import sympy
import matplotlib.pyplot as plt

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

time = np.array([0.163928, 0.53282, 3.00007, 11.2078, 26.7487, 47.3297, 76.8061])
elements = np.array([10, 20, 50, 100, 150, 200, 250])

polynom = newton_poly(time, elements)
polynom(30) #327,....
print(polynom(30))
x = np.linspace(0, 77, 1000)
plt.plot(x, polynom(x))
plt.show()

# The correct solution
# SymPy is a Python library for symbolic computations
from sympy import Symbol, expand, Eq, solve

def newton_poly(nodes, values, x):
    poly = 0
    product = 1
    for i in range(nodes.size):
        poly += divided_difference(nodes[ : i + 1],values[ : i + 1]) * product
        product *= (x - nodes[i])
    return poly

time = np.array([0.163928, 0.53282, 3.00007, 11.2078, 26.7487, 47.3297, 76.8061])
elements = np.array([10, 20, 50, 100, 150, 200, 250])
x = Symbol('x')
left_part = expand(newton_poly(elements, time, x)) 

equation = Eq(left_part, 30) #30 da e reshenie na uravnenieto - demek to e vremeto i tursim x
sol = solve(equation, x)
print(sol)
