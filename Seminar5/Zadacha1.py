import numpy as np
from sympy import symbols, Eq, solve, diff, expand, lambdify
import matplotlib.pyplot as plt

x, y = symbols('x y')
 
def basis_lag(vals, k, symbol):
    prod = 1
 
    for i, val in enumerate(vals):
        if i == k:
            continue
        prod *= (symbol - val) / (vals[k] - val)
    return prod
 
def get_lag_poli_with_two_variables(x_vals, y_vals, results):
    poli = 0
 
    for i in range(len(x_vals)):
        for j in range(len(y_vals)):
            poli += results[i][j] * basis_lag(x_vals, i, x) * basis_lag(y_vals, j, y)
            
    return poli
 
x_vals = np.array([ 0,   2,  4,  6, 8])
y_vals = np.array([ 0,   2,  4,  6, 8])
results = np.array([
    [100.00,    90.00,  80.00,  70.00,  60.00],
    [85.00, 64.49,  53.50,  48.15,  50.00],
    [70.00, 48.90,  38.43,  35.03,  40.00],
    [55.00, 38.78,  30.39,  27.07,  30.00],
    [40.00, 35.00,  30.00,  25.00,  20.00]
])
 
f = lambdify((x, y), get_lag_poli_with_two_variables(x_vals, y_vals, results))
print(f(0, 0))  
print(f(4, 3.2))  
print(f(4.3, 2.7))
