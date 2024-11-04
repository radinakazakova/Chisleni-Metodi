import numpy as np
import math
import sympy

def divided_difference(nodes,values):
    if(len(nodes) == 1):
        return values[0]
    return (divided_difference(nodes[1:], values[1:]) - divided_difference(nodes[:-1], values[:-1])) / (nodes[-1] - nodes[0])

'''
def f(x): #за проверка
    return np.sqrt(x) + 3*x**2 - x + 2

nodes = [0,1,4]
arr = np.array(nodes)
values = f(arr)
res = divided_difference(arr, values)
res
'''
