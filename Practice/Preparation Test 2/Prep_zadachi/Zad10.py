import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

z = sp.symbols('z')
n = sp.symbols('n', positive = True)
x_axis = np.linspace(-2 , -1 , 1000)
threshold = 10 ** (-5)

def f(x):
    return 1 - (1/np.tan(x))
    
def h(x):
    return 1 - sp.cot(x)

def derivativeMax(f, z, num):
    derPoly = sp.lambdify(z, sp.Abs(sp.diff(f(z), z, num)))
    return max(derPoly(x_axis))
    
def rectangle_error_estimate(f, z, b, a, n):
    maxDer = derivativeMax(f, z, 2)
    return maxDer /(24 * (n**2))*((b - a)**3)

def trapezoid_error_estimate(f, z, b, a, n):
    maxDer = derivativeMax(f, z, 2)
    return (maxDer / (12 * n**2)) * ((b-a)**3)

def simpson_error_estimate(f,z, b, a, n):
    maxDer = derivativeMax(f, z, 4)
    return (maxDer /(2880 * (n**4))) * ((b-a)**5)

a = -2
b = -1

errorPolyRect = rectangle_error_estimate(h, z, b, a, n) 
equation_rect = sp.Eq(errorPolyRect, threshold)
sol_rect = sp.solve(equation_rect, n)
integer_N_rect = int(np.ceil(sol_rect[0]))

errorPolyTrap = trapezoid_error_estimate(h, z, b, a, n) 
equation_trap = sp.Eq(errorPolyTrap, threshold)
sol_trap = sp.solve(equation_trap, n)
integer_N_trap = int(np.ceil(sol_trap[0]))

errorPolySimp = simpson_error_estimate(h, z, b, a, n) 
equation_simp = sp.Eq(errorPolySimp, threshold)
sol_simp= sp.solve(equation_simp, n)
integer_N_simp = int(np.ceil(sol_simp[0]))

def rectangle_I(f, b, a , n):
    coef = (b-a)/n
    x_nodes = np.linspace(a, b, n+1)
    expr = 0
    for i in range(len(x_nodes) - 1):
        expr += f((x_nodes[i] + x_nodes[i+1])/2)
    return coef * expr

def trapezoid_I(f, b, a, n):
    coef = (b-a)/(2*n)
    x_nodes = np.linspace(a, b, n+1)
    expr = 0
    for i in range(n):
        expr += (f(x_nodes[i]) + f(x_nodes[i+1]))
    return coef * expr

def simpson_I(f, b, a, n):
    coef = (b-a)/(6*n)
    expr = 0
    x_nodes = np.linspace(a, b, n+1)
    for i in range(n):
        expr += ( f(x_nodes[i]) + 4*f( (x_nodes[i] + x_nodes[i+1]) / 2) + f(x_nodes[i+1]) )
    return coef * expr
    
rect_res = rectangle_I(f, b, a, integer_N_rect)
print(rect_res)

trap_res = trapezoid_I(f, b, a, integer_N_trap)
print(trap_res)

simp_res = simpson_I(f, b, a, integer_N_simp)
print(simp_res)
