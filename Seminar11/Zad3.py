import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, integrate
import sympy

def f(x):
    return 0.2 + 25 * x - 200 * x**2 + 675 * x **3 - 900 * x**4 + 400 * x**5

a = 0
b = 0.8
A1, t1, A2, t2, x= symbols('A1 t1 A2 t2 x')

#2 vuzela
def phi(x):
    return ((b-a)/2) * f((b + a)/ 2 + ((b - a)/2) * x)


equations = [Eq(A1 + A2, integrate(1, (x, -1, 1))), 
            Eq(A1 * t1 + A2 * t2, integrate(x, (x, -1, 1))),
            Eq(A1 * t1 ** 2 + A2 * t2 ** 2, integrate(x ** 2, (x, -1, 1))),
            Eq(A1 * t1 ** 3 + A2 * t2 ** 3, integrate(x ** 3, (x, -1, 1)))]

sol = solve(equations, A1, t1, A2, t2, dict = True)
coef = sol[0]

res = coef[A1] * phi(coef[t1]) + coef[A2] * phi(coef[t2])
sympy.expand(res)

#3 vuzela
B1, x1, B2, x2, B3, x3, x= symbols('B1 x1 B2 x2 B3 x3 x')

equations3 = [Eq(B1 + B2 + B3, integrate(1, (x, -1, 1))), 
            Eq(B1 * x1 + B2 * x2 + B3 * x3, integrate(x, (x, -1, 1))),
            Eq(B1 * x1 ** 2 + B2 * x2 ** 2 + B3 * x3 ** 2, integrate(x ** 2, (x, -1, 1))),
            Eq(B1 * x1 ** 3 + B2 * x2 ** 3 + B3 * x3 ** 3, integrate(x ** 3, (x, -1, 1))),
            Eq(B1 * x1 ** 4 + B2 * x2 ** 4 + B3 * x3 ** 4, integrate(x ** 4, (x, -1, 1))),
            Eq(B1 * x1 ** 5 + B2 * x2 ** 5 + B3 * x3 ** 5, integrate(x ** 5, (x, -1, 1)))]

sol3 = solve(equations3, B1, x1, B2, x2, B3, x3, dict = True)
sol3
coef3 = sol3[0]

res3 = coef3[B1] * phi(coef3[x1]) + coef3[B2] * phi(coef3[x2]) + coef3[B3] * phi(coef3[x3])
sympy.expand(res3)

def trapezoid_I(f, b, a):
    return ((b - a)/2) * (f(a) + f(b))

def simpson_I(f, b, a):
    return ((b - a)/6) * (f(a)+ 4* f((a+b)/2) + f(b))

trap_res = trapezoid_I(f, b, a)
simp_res = simpson_I(f, b, a)
print(trap_res)
print(simp_res)
