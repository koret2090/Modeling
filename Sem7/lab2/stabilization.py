DELTA_T = 1e-3
EPS = 1e-4

def deltaPs(matrix, probabilities):
    size = len(matrix)    
    result = []
    for i in range(size):
        equations = []
        for j in range(size):
            if i == j:
                elem = probabilities[j] * (-sum(matrix[i]) + matrix[i][i])
            else:
                elem = probabilities[j] * matrix[j][i]
            equations.append(elem)
        result.append(DELTA_T * sum(equations))
    return result

def CalculateStabilizationTimings(matrix, firstProbabilities, limitProbabilities):
    size = len(matrix)
    curTime = 0
    currentProbabilities = firstProbabilities.copy()
    stabilizationTimes = [0] * size

    while not all(stabilizationTimes):
        currdeltaPs = deltaPs(matrix, currentProbabilities)
        for i in range(size):
            if (not stabilizationTimes[i] and currdeltaPs[i] <= EPS and 
                    abs(currentProbabilities[i] - limitProbabilities[i]) <= EPS):
                stabilizationTimes[i] = curTime
            currentProbabilities[i] += currdeltaPs[i]

        curTime += DELTA_T

    return stabilizationTimes

def CalculateAllProbabilities(matrix, firstProbabilities, finishTime):
    size = len(matrix)
    curTime = 0
    currentProbabilities = firstProbabilities.copy()

    allProbabilities = []
    timings = []

    while curTime < finishTime:
        allProbabilities.append(currentProbabilities.copy())
        currdeltaPs = deltaPs(matrix, currentProbabilities)
        for i in range(size):
            currentProbabilities[i] += currdeltaPs[i]
        curTime += DELTA_T
        timings.append(curTime)

    return timings, allProbabilities