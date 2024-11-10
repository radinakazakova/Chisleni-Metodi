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

def formula(k,n):
    return np.cos(((2*k - 1)/(2*n))*np.pi) 


def calcChebishoviVuzli(n):
    res = []
    for i in range(1,n):
        res.append(formula(i,n))
    return res

n = 11;
nodes = np.array(calcChebishoviVuzli(n))
values = np.array(f(nodes))
polynom = newton_poly(nodes, values)

def abs_error(z):
    return np.abs(f(z) - polynom(z))

x = np.linspace(-1,1,100)
plt.plot(x,f(x))
plt.plot(x, polynom(x))
plt.legend(['f(x)','interpolating polynomial'])
plt.show()
plt.plot(x, abs_error(x))
plt.legend(['Absolute error'])
plt.show()
