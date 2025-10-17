def createMatrix(values):
    size = len(values)
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append( np.e ** (j * values[i]))
        matrix.append(row)
    return np.array(matrix)
