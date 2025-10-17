import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

a = 7
b = 9

z = sp.symbols('z')

def f(x):
    return np.sin(x)/ np.log(x)

def rectangle_I(f, b, a):
    return (b - a) * f((a+b)/2)

def trapezoid_I(f, b, a):
    return ((b - a)/2) * (f(a) + f(b))

def simpson_I(f, b, a):
    return ((b - a)/6) * (f(a)+ 4* f((a+b)/2) + f(b))

rect = rectangle_I(f, b, a)
trap = trapezoid_I(f, b, a)
simp = simpson_I(f, b, a)

x_axis = np.linspace(7, 9, 1000)
plt.plot(x_axis, f(x_axis))
plt.show()
rect #0.9515614907107686
trap #0.5251875296832664
simp #0.8094368370349345
res, error = scipy.integrate.quad(f, a, b)
res #0.804964022751974 
#симпсън пресмята с най-голяма точност
