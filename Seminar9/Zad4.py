from sympy import symbols, diff, solve, Eq
import numpy as np
import matplotlib.pyplot as plt
x, y = symbols('x, y')

def objective(x, y):
    return (x - y - 1) ** 2 + (x + y - 1) ** 2 + (x + y + 1) ** 2 + (x - y + 1) ** 2

func = objective(x,y)
sol = solve([Eq(diff(func, x), 0),
             Eq(diff(func, y), 0)])
sol
