import numpy as np
import sympy as sp
import scipy
import matplotlib.pyplot as plt

xs = np.array([1, 1.5, 2, 3, 3.5, 4, 5, 8])
ys = np.array([2.2, 2.5, 3.2, 3.6, 4.1, 4.5, 4.5, 6])

a,b,c = sp.symbols('a b c')

def f(x, param):
    a,b,c = param
    return a + b*x + c/x

def findPhi(f):
    n = len(xs)
    expr = 0
    for i in range(n):
        expr += (f(xs[i], (a,b,c)) - ys[i]) ** 2
    return sp.expand(expr)

phi = findPhi(f)
sol = sp.solve([sp.Eq(sp.diff(phi, a), 0),
                sp.Eq(sp.diff(phi, b), 0),
                sp.Eq(sp.diff(phi, c), 0)])

x_axis = np.linspace(1, 8, 100)
plt.scatter(xs, ys)
plt.plot(x_axis, f(x_axis, (sol[a], sol[b], sol[c])), 'red')
plt.show()
