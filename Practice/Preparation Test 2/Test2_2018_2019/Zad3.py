from sympy import symbols, diff, solve, Eq
import numpy as np
import matplotlib.pyplot as plt
x, y = symbols('x, y')

def objective(x, y):
    return (x + 2*y - 1) ** 2 + (x - y - 5) ** 2 + (3*x + 4*y - 17) ** 2

func = objective(x, y)
sol = solve([Eq(diff(func, x), 0),
             Eq(diff(func, y), 0)])
sol
