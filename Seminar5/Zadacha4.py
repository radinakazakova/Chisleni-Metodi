import numpy as np
import math
import matplotlib.pyplot as plt
def newton_forward(n, x0, h, f_values):
    differences = [f_values]
    for i in range(1, n + 1):
        diff = [differences[-1][j + 1] - differences[-1][j] for j in range(len(differences[-1]) - 1)]
        differences.append(diff)

    def polynomial(x):
        result = differences[0][0]
        factorial = 1
        product = 1
        for i in range(1, n + 1):
            factorial *= i
            product *= (x - (x0 + (i - 1) * h))
            result += (differences[i][0] / factorial) * product
        return result
    return polynomial

def f(x):
    return np.cos(np.radians(x))

x_nodes = np.array([45, 50, 55, 60])
y_values = np.array(f(x_nodes))
poly = newton_forward(3, math.radians(45), 5, y_values)

poly(52)
#x_axis = np.linspace(45, 60, 1000)
#plt.plot(x_axis, poly(np.radians(x_axis)))
#plt.show()


# or 

import math

def newton_forward_cos(x_target, x_nodes, n=3):
    # Стойности на cos(x) за дадените възли
    f_values = [math.cos(math.radians(x)) for x in x_nodes]

    # Изчисляваме таблица на крайните разлики
    differences = [f_values]
    for i in range(1, n + 1):
        diff = [differences[-1][j + 1] - differences[-1][j] for j in range(len(differences[-1]) - 1)]
        differences.append(diff)

    # Изграждаме полинома
    x0 = x_nodes[0]
    h = x_nodes[1] - x_nodes[0]

    result = differences[0][0]  # Начална стойност f(x0)
    factorial = 1
    product = 1
    for i in range(1, n + 1):
        factorial *= i
        product *= (x_target - (x0 + (i - 1) * h))
        result += (differences[i][0] / factorial) * product
    
    return result

x_nodes = [45, 50, 55, 60]
x_target = 52

cos_52 = newton_forward_cos(x_target, x_nodes)
cos_52
