import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return x**3

a = 0.5
b = 1.5

#za pravougulnici
z = sp.Symbol('z')

def I(f, b, a):
    return (b - a) * f((a+b)/2)

f = z**3

def rectangle_error_estimate(f, z, b, a):
    return (np.abs(sp.diff(f, z, 2))/ 24) * (b - a)**3

errorPoly = sp.lambdify(z, rectangle_error_estimate(f, z, b, a))
x_axis = np.linspace(0.5, 1.5, 1000)
maxError = max(errorPoly(x_axis))
maxError #0.375 = 3/8

res = I(h, b, a)
res # 1 -> грешката е 0.25

#трапеци
import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

a = 0.5
b = 1.5

#za pravougulnici
z = sp.Symbol('z')

def I(f, b, a):
    return ((b - a)/2) * (f(a) + f(b))

def trapezoid_error_estimate(f, z, b, a):
    return (np.abs(-(sp.diff(f(z), z, 2)))/12) * (b - a)**3

errorPoly = sp.lambdify(z, trapezoid_error_estimate(f, z, b, a))
x_axis = np.linspace(0.5, 1.5, 1000)
maxError = max(errorPoly(x_axis))
maxError # 0.75

res = I(h, b, a)
res # 1.75 -> грешката е 0.5

#симпсън
import sympy as sp
import scipy #scipy.integrate.quad
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

a = 0.5
b = 1.5

def I(f, b, a):
    return ((b - a)/6) * (f(a)+ 4* f((a+b)/2) + f(b))

def simpson_error_estimate(f, z, b, a):
    return (np.abs(-(sp.diff(f(z), z, 4)))/2880) * (b-a)**5

errorPoly = simpson_error_estimate(f, z, b, a)
#x_axis = np.linspace(0.5, 1.5, 1000)
#maxError = max(errorPoly(x_axis))
#maxError
errorPoly #0 -> симпсън работи точно до 3та степен

res = I(f, b, a)
res #1.25 -> грешката е 0
