import math
import numpy as np
from sympy import symbols, Eq, solve, diff, expand, lambdify, cos
import matplotlib.pyplot as plt
 
#зад 3
 
def calculate_p(x0, h):
    return (x - x0) / h
 
 
def calc_devided_diff(x0, h, i, f, pow):
    if pow == 0:
        return 1
        
    if pow == 1:
        return f((x0 + (i+1)*h)) - f((x0 + i*h))
 
    return calc_devided_diff(x0, h, i+1, f, pow-1) - calc_devided_diff(x0, h, i, f, pow-1)
 
 
def get_newton_forward_poli(n, x0, h, f):
    poli = 0
    curr_p = 1
    
    for i in range(n):
        dd = calc_devided_diff(x0, h, i, f, i)
        print(dd)
        poli += (f(x0) * dd * curr_p) / math.factorial(i)
        curr_p *= (calculate_p(x0,h) - i)
    return poli
        
 
#зад 4
x_vals = np.array([45,50,55,60])
y_vals = np.array([np.cos(np.radians(el) )for el in [45,50,55,60]])
x0 = 45
n = len(x_vals)
h = 5
def cos_deg(x):
    return np.cos(np.radians(x))
f = lambdify(x, get_nuton_forward_poli(4, x0, h, cos_deg))
print(f(52), np.cos(np.radians(52)))
 
 
x_ax = np.linspace(45,60,1000) # np.linspace(<begin>, <end>, <count>) - равно раздаличени точки
plt.plot(x_ax, f(x_ax))        # plt.plot(x_arr, y_arr) - прави графиката
plt.scatter(x_vals,y_vals)     # plt.scatter(x_arr, y_arr) - поставя точки на графиката
plt.show() 
