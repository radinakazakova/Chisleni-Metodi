import numpy as np
import math
import matplotlib.pyplot as plt

#construct the interpoalting polynomial
x0 = 0;
x1 = math.pi/6;
x2 = math.pi/3;
x3 = math.pi/2;

def f(x):
    return np.sin(x)

y0 = f(x0);
y1 = f(x1);
y2 = f(x2);
y3 = f(x3);

def l0(x):
    return (x - x1)*(x - x2)*(x - x3)/((x0 - x1)*(x0 - x2)*(x0 - x3))
def l1(x):
    return (x - x0)*(x - x2)*(x - x3)/((x1 - x0)*(x1 - x2)*(x1 - x3))
def l2(x):
    return (x - x0)*(x - x1)*(x - x3)/((x2 - x0)*(x2 - x1)*(x2 - x3))
def l3(x):
    return (x - x0)*(x - x1)*(x - x2)/((x3 - x0)*(x3 - x1)*(x3 - x2))

def L3(x):
    return y0 * l0(x) + y1 * l1(x) + y2 * l2(x) + y3 * l3(x)

#compute the approximation 
exact_value = math.sin(math.pi/5)
approx_value = L3(math.pi/5)
error_estimate = 1/24 * abs(math.pi/5 * (math.pi/5 - math.pi/6) * (math.pi/5 - math.pi/3) * (math.pi/5 - math.pi/2))
print("Exact value: ", exact_value)
print("Approx value: ", approx_value)
print("Absolute error: ", abs(exact_value - approx_value))
print("Error estimate: ", error_estimate)

#plot data
nodes = np.array([0, math.pi/6, math.pi/3, math.pi/2])
f_values = np.sin(nodes)
plt.scatter(nodes, f_values)
x_axis = np.linspace(0, math.pi/2, 1000)
plt.plot(x_axis, np.sin(x_axis), color='y')
plt.plot(x_axis, L3(x_axis), color='black', linestyle='dashed')
plt.xlabel('x')
plt.legend(['data','sin(x)',' L3(f;x)'])
plt.show()


#plot errors as functions of  x
def abs_error_func(x):
    return abs(f(x) - L3(x))

def error_estimate(x):
    return 1/24 * abs(x * (x - math.pi/6) * (x - math.pi/3) * (x - math.pi/2))

plt.plot(x_axis, abs_error_func(x_axis))
plt.legend(['Absolute error'])
plt.show()
plt.plot(x_axis, abs_error_func(x_axis))
plt.plot(x_axis, error_estimate(x_axis))
plt.legend(["Absolute error","Error estimate"])
plt.show()
