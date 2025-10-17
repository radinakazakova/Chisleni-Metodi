from sympy import symbols, diff, solve, Eq
import numpy as np
import matplotlib.pyplot as plt
x, y, z = symbols('x, y, z')

#има грешка в системата
#трябва да е 2х на първото уравнение
def objective(x, y, z):
    return (2*x + y + z - 1)**2 + (x + 2*y + z - 2)**2 + (x + 3*y+ z - 3)**2 + (x - 4*y + z - 4)**2 + (x + 5*y + z - 4)**2

func = objective(x,y,z)
sol = solve([Eq(diff(func, x), 0),
             Eq(diff(func, y), 0),
             Eq(diff(func, z), 0)])
sol
