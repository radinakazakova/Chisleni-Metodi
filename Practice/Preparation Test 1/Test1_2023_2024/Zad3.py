import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

x = sp.symbols('x')

def calcNodes(n, A, B):
    return np.linspace(A,B, n+1)

def Lagrange(n, A, B, f, x):
    nodes = calcNodes(n, A, B)
    res = 0
    for k in range(n + 1):
        Lk = 1
        for i in range(n + 1):
            if k != i:
                Lk *= (x - nodes[i]) / (nodes[k] - nodes[i])

        print(Lk)
        res += f(nodes[i]) * Lk
    return res
        
def f(z):
    return (z**2)/3 + z*2
    
ans = Lagrange(3, 15, 20, f, x)
sp.expand(ans)
