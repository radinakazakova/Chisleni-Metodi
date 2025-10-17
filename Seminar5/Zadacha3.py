def newton_forward(n, x0, h, f):
        differences = [f]
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
