import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import sympy as sp
import scipy

a = -np.pi
b = 0

A1, A2, A3, x1, x2, x3,x = sp.symbols('A1, A2, A3, x1, x2, x3, x')
def f(x):
    return np.cos(x) ** 3 + 141

def phi(x):
    return (b-a)/2 * f((b + a)/2 + ((b - a)/2) * x)

equations = [sp.Eq(A1 + A2 + A3, sp.integrate(1, (x, -1, 1))),
             sp.Eq(A1 * x1 + A2 * x2 + A3 * x3, sp.integrate(x, (x, -1, 1))),
             sp.Eq(A1 * x1**2 + A2 * x2**2 + A3 * x3**2, sp.integrate(x**2, (x, -1, 1))),
             sp.Eq(A1 * x1**3 + A2 * x2**3 + A3 * x3**3, sp.integrate(x**3, (x, -1, 1))),
             sp.Eq(A1 * x1**4 + A2 * x2**4 + A3 * x3**4, sp.integrate(x**4, (x, -1, 1))),
             sp.Eq(A1 * x1**5 + A2 * x2**5 + A3 * x3**5, sp.integrate(x**5, (x, -1, 1))),]
sol = sp.solve(equations, A1, A2, A3, x1, x2, x3, dict = True)
nums = sol[2]
res = nums[A1] * phi(float(nums[x1])) + nums[A2] * phi(float(nums[x2])) + nums[A3] * phi(float(nums[x3]))
res1, error = scipy.integrate.quad(f, a, b)
print("Value from Legendre: ",res)
print("Exact value: ",res1)

##
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, integrate
import sympy as sp

x, A1, A2, A3, x1, x2, x3 = symbols('x, A1, A2, A3, x1, x2, x3')
a = -np.pi
b = 0

def f(x):
    return sp.cos(x) ** 3 + 141

equations = [Eq(A1 + A2 + A3, integrate(1, (x, a, b))), 
            Eq(A1 * x1 + A2 * x2 + A3 * x3, integrate(x, (x, a, b))),
            Eq(A1 * x1 ** 2 + A2 * x2 ** 2 + A3 * x3 ** 2, integrate(x ** 2, (x, a, b))),
            Eq(A1 * x1 ** 3 + A2 * x2 ** 3 + A3 * x3 ** 3, integrate(x ** 3, (x, a, b))),
            Eq(A1 * x1 ** 4 + A2 * x2 ** 4 + A3 * x3 ** 4, integrate(x ** 4, (x, a, b))),
            Eq(A1 * x1 ** 5 + A2 * x2 ** 5 + A3 * x3 ** 5, integrate(x ** 5, (x, a, b)))]
