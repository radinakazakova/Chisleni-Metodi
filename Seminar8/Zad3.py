import pandas as pd

df = pd.read_csv('other_files/wind_turbine_data_sample.csv')
xs = np.array( df['wind speed'])
ys = np.array( df['power output'])

a,b,c,d = symbols('a, b, c, d')

def f(x, param):
    a,b,c,d = param
    return a* (x**3) + b* (x**2) + c*x + d

def findPhi(f):
    expr = 0
    for i in range(len(xs)):
        expr += (f(xs[i], (a,b,c,d)) - ys[i]) ** 2
    expand(expr)
    return expr
    
phi = findPhi(f)

sol = solve([Eq(diff(phi,a), 0),
             Eq(diff(phi,b), 0),
             Eq(diff(phi,c), 0),
             Eq(diff(phi,d), 0)])

x_axis = np.linspace(5, 13, 1000)
plt.scatter(xs, ys)
plt.plot(x_axis, f(x_axis, (sol[a], sol[b], sol[c], sol[d])), 'red')
plt.show()
