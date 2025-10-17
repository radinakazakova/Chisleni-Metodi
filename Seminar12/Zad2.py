import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#cos(x) = x
def f(x):
    return np.cos(x) - x
z = sp.symbols('z')
h = sp.cos(z) - z

a = 0
b = 1
x0 = 0
epsilon = 10 ** (-5)


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

res, iterations = newton(x0) #резултата е в интервала [0,1]
print("Root approximately - newton:", res)
print("Number of iterations - newton:", iterations)
x_axis = np.linspace(a,b, 1000)
y_axis = f(x_axis)
plt.plot(x_axis, y_axis)
plt.scatter(res, f(res))
plt.show()

#e^x -x^4
def f(x):
    return np.e**x - x**4

z = sp.symbols('z')
h = sp.exp(z) - z**4

a = 0.5
b = 1.5
epsilon = 10 ** (-5)

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

x0 = (a+b)/2
res, iterations = newton(x0)
print("Root approximately - newton:", res)
print("Number of iterations - newton:", iterations)
x_axis = np.linspace(a,b, 1000)
y_axis = f(x_axis)
plt.plot(x_axis, y_axis)
plt.scatter(res, f(res))
plt.show()

#e^x -x^4
def f(x):
    return np.e**x - x**4

z = sp.symbols('z')
h = sp.exp(z) - z**4

a = -1.5
b = -0.5
epsilon = 10 ** (-5)

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

x0 = (a+b)/2
res, iterations = newton(x0)
print("Root approximately - newton:", res)
print("Number of iterations - newton:", iterations)
x_axis = np.linspace(a,b, 1000)
y_axis = f(x_axis)
plt.plot(x_axis, y_axis)
plt.scatter(res, f(res))
plt.show()

#e^x -x^4
def f(x):
    return np.e**x - x**4

z = sp.symbols('z')
h = sp.exp(z) - z**4

a = 7
b = 9
epsilon = 10 ** (-5)

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

x0 = (a+b)/2
res, iterations = newton(x0)
print("Root approximately - newton:", res)
print("Number of iterations - newton:", iterations)

x_axis = np.linspace(a,b, 1000)
y_axis = f(x_axis)
plt.plot(x_axis, y_axis)
plt.scatter(res, f(res))
plt.show()

#x*(x-1)*(x+1)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def f(x):
    return x*(x-1)*(x+1)

z = sp.symbols('z')
h = z * (z-1)*(z+1)

a = 0.55
b = 1.1
epsilon = 10 ** (-5)

def getDer(h, z):
    return sp.lambdify(z, sp.diff(h, z))

def newton(x0):
    der = getDer(h, z)
    iter_n = 0

    while iter_n < 5:
        if(der(x0) == 0):
            return (-1, -1)
    
        x_next = x0 - (f(x0))/der(x0)
        iter_n += 1
    
        x0 = x_next  
    return x_next, iter_n

x0 = a
res, iterations = newton(x0)
print("Root approximately - newton:", res)
print("Number of iterations - newton:", iterations)

x_axis = np.linspace(a,b, 1000)
y_axis = f(x_axis)
plt.plot(x_axis, y_axis)
plt.scatter(res, f(res))
plt.show() #не работи с нютон май
