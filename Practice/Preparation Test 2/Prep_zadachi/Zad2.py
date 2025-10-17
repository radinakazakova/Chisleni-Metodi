import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

xs = np.array([0.2, 0.5, 0.8, 1.2, 1.7, 2, 2.3])
ys = np.array([500, 700, 1000, 1200, 2200, 2650, 3750])

#tursim parabola
power = 2

A = np.zeros([power+1, power+1]) #matrix (with zeros)
b = np.zeros([power+1]) #in equation -> right column (with zeros)

def f(x, coef):
    return coef[0] + coef[1]*x + coef[2]*(x**2)

def calc_A_and_b(power):
    s = len(xs)
    for row in range(power+1):
        for k in range(s):
            b[row] += xs[k] ** row * ys[k]
            for col in range(power+1):
                A[row, col] += xs[k] ** (row + col)

calc_A_and_b(power)
coef = np.array(np.linalg.solve(A, b))
x_axis = np.linspace(0.2, 2.3, 100)
plt.scatter(xs, ys)
plt.plot(x_axis, f(x_axis, coef))
plt.show()
