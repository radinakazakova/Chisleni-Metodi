import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, expand, diff
#nai-veroqtno shte ima takava na vtoroto kontrolno
#f(x) = a*x + b
#y = a * e ** bx
#problem b e v stepenen pokazatel, pri diff shte se izvurshat slojni operacii koito shte budat problem - izbqgvame da gi reshawame (rqdko mojem da im namerim tochnoto reshnie)
# ln y = ln a + bx (ln a = c)
#tyrsim : f(x) = c + bx
#phi(a,b) = suma (f(xi) - lnyi)**2 = suma (c+bxi - ln yi)** 2
# yi = e^(c + bxi)

df = pd.read_csv('other_files/amazon_sales_net_revenue.csv')
xs = np.array(df['year'])
ys = np.array(df['revenue'])

c, b = symbols('c,b')

def f(x, param):
    b,c = param
    return b*x + c

def findPhi(f):
    expr = 0
    for i in range(len(xs)):
        expr += (f(xs[i], (b, c)) - np.log(ys[i])) ** 2
    expand(expr)
    return expr
    
phi = findPhi(f)

sol = solve([Eq(diff(phi,b), 0),
             Eq(diff(phi,c), 0)])

def exp_func(x):
    return np.exp(float(sol[b])*x + float(sol[c]))

x_axis = np.linspace(2004, 2021, 100)
plt.plot(x_axis, exp_func(x_axis), 'red')
plt.scatter(xs, ys)
plt.show()
