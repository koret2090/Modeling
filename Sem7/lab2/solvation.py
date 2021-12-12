import numpy

def coefMatrixGenerate(matrix):
    matrix = numpy.array(matrix)
    size = len(matrix)
    result = numpy.zeros((size, size))

    for state in range(size - 1):
        for column in range(size):
            result[state, state] -= matrix[state, column]
        for row in range(size):
            result[state, row] += matrix[row, state]

    for state in range(size):
        result[size - 1, state] = 1

    return result

def createIncreaseMatrix(count):
    result = [0] * count
    result[count - 1] = 1
    return numpy.array(result)

def solve(matrix):
    increaseMatrix = createIncreaseMatrix(len(matrix))
    coefMatrix = coefMatrixGenerate(matrix)
    return numpy.linalg.solve(coefMatrix, increaseMatrix)