import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

z = sp.symbols(' z')
n = sp.symbols('n', positive = True)
x_axis = np.linspace(1, 2, 1000)
threshold = 10** (-5)

def f(x):
    return (1/x)

def derivativeMax(f, z, num):
    poly = sp.lambdify(z, sp.Abs(sp.diff(f(z), z, num)))
    return max(poly(x_axis))
    
def rectangle_error_estimate(f, z, b, a, n):
    maxDerivative = derivativeMax(f, z, 2)
    return maxDerivative /(24 * (n**2))*((b - a)**3)

a = 1
b = 2

#x_nodes = np.linspace(a, b, n + 1)
errorPoly = rectangle_error_estimate(f, z, b, a, n) #полином с променлива 'n'
#N = int(np.ceil( np.sqrt(10**5/12))) #след преобразувания търсим ceiling на уравнението, за да намерим n, тъй като имаме n >= ... (намираме за равното и търсим кое е най-близкото цяло число)
equation = sp.Eq(errorPoly, threshold)
sol = sp.solve(equation, n)
integer_N = int(np.ceil(sol[0]))

def rectangle_I(f, b, a , n):
    coef = (b-a)/n
    x_nodes = np.linspace(a, b, n+1)
    expr = 0
    for i in range(len(x_nodes) - 1):
        expr += f((x_nodes[i] + x_nodes[i+1])/2)
    return coef * expr

rect_res = rectangle_I(f, b, a, integer_N)
rect_res #0.6931434885476101

#трапеци

import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

z = sp.symbols('z')
n = sp.symbols('n', positive = True)
threshold = 10 ** (-5)

x_axis = np.linspace(1, 2, 1000)

def f(x):
    return (1/x)

def derivativeMax(f, z, num):
    poly = sp.lambdify(z, sp.Abs(sp.diff(f(z), z, num)))
    return max(poly(x_axis))

def trapezoid_error_estimate(f, z, b, a, n):
    maxDer = derivaerrorPoly = rectangle_error_estimate(f, z, b, a, n) #полином с променлива 'n'
#N = int(np.ceil( np.sqrt(10**5/12))) #след преобразувания търсим ceiling на уравнението, за да намерим n, тъй като имаме n >= ... (намираме за равното и търсим кое е най-близкото цяло число)
equation = sp.Eq(errorPoly, threshold)
sol = sp.solve(equation, n)
integer_N = int(np.ceil(sol[0]))

def rectangle_I(f, b, a , n):
    coef = (b-a)/n
    x_nodes = np.lintiveMax(f, z, 2)
    return (maxDer / (12 * n**2)) * ((b-a)**3)

a = 1
b = 2
errorPoly = trapezoid_error_estimate(f, z, b, a, n)
errorPoly # 1/6n**2
# errorPoly <= 10** -5
# n >= sqrt(10**5 / 6)
N = int(np.ceil( np.sqrt(10**5/6) ))
equation = sp.Eq(errorPoly, threshold)
sol = sp.solve(equation, n)
integer_N = int(np.ceil(sol[0]))

def trapezoid_I(f, b, a, n):
    coef = (b-a)/(2*n)
    x_nodes = np.linspace(a, b, n+1)
    expr = 0
    for i in range(n):
        expr += (f(x_nodes[i]) + f(x_nodes[i+1]))
    return coef * expr

trap_res = trapezoid_I(f, b, a, integer_N)
trap_res

#Симпън
import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

z = sp.symbols('z')
n = sp.symbols('n', positive = True)
x_axis = np.linspace(1, 2, 1000)
threshold = 10 ** (-5)
def f(x):
    return (1/x)

def derivativeMax(f, z, num):
    poly = sp.lambdify(z, sp.Abs(sp.diff(f(z), z, num)))
    return max(poly(x_axis))

def simpson_error_estimate(f,z, b, a, n):
    maxDer = derivativeMax(f, z, 4)
    return (maxDer /(2880 * (n**4))) * ((b-a)**5)

a = 1
b = 2
errorPoly = simpson_error_estimate(f, z, b, a, n)
equation = sp.Eq(errorPoly, threshold)
sol = sp.solve(equation, n)
integer_N = int(np.ceil(sol[0]))

def simpson_I(f, b, a, n):
    coef = (b-a)/(6*n)
    expr = 0
    x_nodes = np.linspace(a, b, n+1)
    for i in range(n):
        expr += ( f(x_nodes[i]) + 4*f( (x_nodes[i] + x_nodes[i+1]) / 2) + f(x_nodes[i+1]) )
    return coef * expr

simp_res = simpson_I(f, b, a, integer_N)
simp_res
