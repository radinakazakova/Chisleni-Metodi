import numpy as np

def lagrange_interpolation(x, x_nodes, y_nodes):
    result = 0
    n = len(x_nodes)
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

def lookup_table_f(x_val):
    h = 0.01
    f_nodes = np.arange(0, 2 * np.pi + h, h)
    f_values = np.sin(np.sqrt(f_nodes))

    if x_val < 0 or x_val > 2 * np.pi:
        return "Грешка: x_val е извън интервала [0, 2π]"

    if x_val <= 0.01:
        closest_indices = [0, 1, 2, 3]
    elif x_val >= 2 * np.pi - 0.01:
        closest_indices = [-4, -3, -2, -1]
    else:
        idx = np.searchsorted(f_nodes, x_val) #namira nai-blizkiq > x_val
        closest_indices = [idx - 2, idx - 1, idx, idx + 1]

    x_closest = f_nodes[closest_indices]
    y_closest = f_values[closest_indices]

    return lagrange_interpolation(x_val, x_closest, y_closest)

x_val = 0.3
result = lookup_table_f(x_val)
print(f"f({x_val}) = {result}")
print(np.sin(np.sqrt(x_val)))
    
