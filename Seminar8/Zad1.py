import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff

xs = np.array([0, 1, 2, 3, 4])
ys = np.array([0, 1, 1, 2, 2])

a,b = symbols('a, b')

def f(x, param):
    a,b = param
    return a * x + b

#phi = 0
#for i in range(len(xs)):
#    phi += (f(xs[i], (a,b)) - ys[i]) ** 2
#expand(phi)

def findPhi(f):
    expr = 0
    for i in range(len(xs)):
        expr += (f(xs[i], (a,b)) - ys[i]) ** 2
    expand(expr)
    return expr
    
phi = findPhi(f)
sol = solve([Eq(diff(phi, a), 0),
             Eq(diff(phi, b), 0)])


f(0.1, (sol[a], sol[b]))

x_axis = np.linspace(0, 4, 100)
plt.plot(x_axis, f(x_axis, (sol[a], sol[b])))
plt.scatter(xs, ys)
plt.show()
