import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

a = 0
b = 3
epsilon = 10 ** (-5)

def f(x):
    return np.exp(x) - 3
    
z = sp.symbols('z')
h = sp.exp(z) - 3

#метод на разполовяването

def bisection(a, b, bisection_iterations):
    while np.abs(b - a) > epsilon:
        bisection_iterations += 1  
        mid = (a + b) / 2  
        if f(mid) < 0:
            a = mid  
        else:
            b = mid  
    return (a, bisection_iterations)  

bisection_iterations = 0  
res, bi = bisection(a, b, bisection_iterations)
print("Root approximately:", res)
print("Number of iterations:", bi)

#метод на Нютон

x0 = (a+b)/2

def getDer(h, z):
    return sp.lambdify(z, sp.diff(h, z))

def newton(x0):
    der = getDer(h, z)
    iter_n = 0

    while True:
        if(der(x0) == 0):
            return (-1, -1)
    
        x_next = x0 - (f(x0))/der(x0)
        iter_n += 1
    
        if np.abs(x_next - x0) < epsilon:
            return x_next, iter_n
        
        x0 = x_next  

n, iter_n = newton(x0)
print("Root approximately - newton:", n)
print("Number of iterations - newton:", iter_n)
