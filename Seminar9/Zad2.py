import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def least_squares_matrix(x, y, n): 
    A = np.zeros([n+1, n+1])
    b = np.zeros([n+1])
    s = len(x)
    for row in range(n+1):
        for k in range(s):
            b[row] += x[k]**row * y[k]
            for col in range(n+1):
                A[row, col] += x[k] ** (row + col)

    coefs = np.linalg.solve(A,b)
    return coefs
