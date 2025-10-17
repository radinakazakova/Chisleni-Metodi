import numpy as np
import sympy as sp
import scipy
import matplotlib.pyplot as plt

x1 = -np.sqrt(1/3)
x2 = np.sqrt(1/3)

A1 = 1
A2 = 1

def f(x):
    return (np.e**x) * np.cos(x)

a = -1
b = 1

res = A1 * f(x1) + A2 * f(x2)
res # ACT 3
