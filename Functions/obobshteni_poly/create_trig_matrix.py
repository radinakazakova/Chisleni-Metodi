def createTrigMatrix(values):
    size = len(values)
    matrix = []
    for i in range(size):
        row = []
        counter = 1
        for j in range(size):
            if j == 0:
                row.append(1)
            elif j % 2 != 0:
                row.append( np.cos(counter * values[i]) )
            else:
                row.append( np.sin(counter * values[i]) )
                counter += 1
        matrix.append(row)
    return np.array(matrix)


def changePeriod(t, values):
    return np.array([((2*np.pi)/t)*el for el in values])
