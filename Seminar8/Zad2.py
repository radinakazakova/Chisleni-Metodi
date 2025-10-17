import pandas as pd

df = pd.read_csv('other_files/CO_2_data.csv')
xs = np.array( df['year'])
ys = np.array( df['co2'])

a,b = symbols('a, b')

def f(x, param):
    a,b = param
    return a * x + b

def findPhi(f):
    expr = 0
    for i in range(len(xs)):
        expr += (f(xs[i], (a,b)) - ys[i]) ** 2
    expand(expr)
    return expr
    
phi = findPhi(f)

sol = solve([Eq(diff(phi, a), 0),
             Eq(diff(phi, b), 0)])

x_axis = np.linspace(1944, 2022, 80)
plt.plot(x_axis, f(x_axis, (sol[a], sol[b])))
plt.scatter(xs, ys)
plt.show()
