import numpy as np
import math

def lagrange_poly(f, nodes, x):
    n = len(nodes)
    result = 0

    for k in range(n):
        Lk = 1
        for j in range(n):
            if k != j:
                Lk *= (x - nodes[k]) / (nodes[k] - nodes[j])

        result += f(nodes[k]) * Lk

return result
