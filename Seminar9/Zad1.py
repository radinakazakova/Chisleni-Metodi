#a0 + a1x
import numpy as np
import matplotlib.pyplot as plt

xs = np.array([0, 1, 2, 3, 4])
ys = np.array([0, 1, 1, 2, 2])

#ako znaem stepenta, s koqto rabotim, imame
power = 1
A = np.zeros([power+1, power+1]) #matrix (with zeros)
b = np.zeros([power+1]) #in equation -> right column (with zeros)

def f(x, coef):
    return coef[0] + coef[1]*x

def calc_A_and_b(power):
    s = len(xs)
    for row in range(power+1):
        for k in range(s):
            b[row] += xs[k] ** row * ys[k]
            for col in range(power+1):
                A[row, col] += xs[k] ** (row + col)

calc_A_and_b(power)
coef = np.array(np.linalg.solve(A,b))
x_axis = np.linspace(0,4, 100)
plt.scatter(xs, ys)
plt.plot(x_axis, f(x_axis, coef))
plt.show()
