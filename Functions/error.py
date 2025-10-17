import numpy as np
from sympy import symbols, Eq, solve, diff, expand, lambdify, Abs
import matplotlib.pyplot as plt
import math
 
x = symbols('x')
 
def error(x_vals, f, val):
    second_part = 1
    for xi in x_vals:
        second_part *= (val - xi)
    return (Abs(diff(f, x, len(x_vals)) / math.factorial(len(x_vals)))) * Abs(second_part)    
 
error([0,1], 1/(x+1), 0.75)

import numpy as np
from sympy import symbols, Eq, solve, diff, expand, lambdify, Abs
import matplotlib.pyplot as plt
import math
 
z, x = symbols('z, x')
f = 1/(z+1)

def get_second_part(x_vals):
    expr = 1
    for xi in x_vals:
        expr *= (x - xi)
    return Abs(expr)

def get_first_part(x_vals, f):
    return (Abs(diff(f, z, len(x_vals)) / math.factorial(len(x_vals))))

first = lambdify(z, get_first_part([0,1], f))
second = lambdify(x, get_second_part([0,1]))

x_axis = np.linspace(0, 1, 1000)
getMaxFirst = np.max( first(x_axis) )
getMaxSecond = np.max( second(x_axis))
getRes = getMaxFirst * getMaxSecond
getRes # ocenkata e ravna na ili ne nadvishava getRes
