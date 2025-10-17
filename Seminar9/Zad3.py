#zadacha 2
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import pandas as pd

df = pd.read_csv('other_files/CO_2_data.csv')
xs = np.array( df['year'])
ys = np.array( df['co2'])

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

def f(x, coef):
    size = len(coef)
    power = 0
    res = 0
    for i in range(size):
        res += coef[i] * (x ** power)
        power += 1
    return res
        
coef = least_squares_matrix(xs, ys, 1)
x_axis = np.linspace(1944, 2022, 80)
plt.plot(x_axis, f(x_axis, coef))
plt.scatter(xs, ys)
plt.show()

#zadacha 3
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import pandas as pd

df = pd.read_csv('other_files/wind_turbine_data_sample.csv')
xs = np.array( df['wind speed'])
ys = np.array( df['power output'])

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

def f(x, coef):
    size = len(coef)
    power = 0
    res = 0
    for i in range(size):
        res += coef[i] * (x ** power)
        power += 1
    return res

coef = least_squares_matrix(xs, ys, 3)
x_axis = np.linspace(5, 13, 1000)
plt.scatter(xs, ys)
plt.plot(x_axis, f(x_axis, coef), 'red')
plt.show()

#zadacha 4
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
import pandas as pd

df = pd.read_csv('other_files/amazon_sales_net_revenue.csv')
xs = np.array(df['year'])
ys = np.array(df['revenue'])

def least_squares_matrix(x, y, n): 
    A = np.zeros([n+1, n+1])
    b = np.zeros([n+1])
    s = len(x)
    for row in range(n+1):
        for k in range(s):
            b[row] += x[k]**row * np.log(y[k])
            for col in range(n+1):
                A[row, col] += x[k] ** (row + col)

    coefs = np.linalg.solve(A,b)
    return coefs

coef = least_squares_matrix(xs, ys, 1)

def exp_func(x): 
    return np.exp(coef[0] + coef[1]*x)

x_axis = np.linspace(2004, 2021, 100)
plt.plot(x_axis, exp_func(x_axis), 'red')
plt.scatter(xs, ys)
plt.show()
