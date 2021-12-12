from time import time
from UniformDistribution import UniformDistribution
from Generator import Generator
from Operator import Operator
from Processor import Processor

timeStep = 0.01  # еденица системного времени - 0.01 минуты


def ChooseOperator(operators):
    for i in range(len(operators)):
        if not operators[i].busy:
            return i
    return -1

def DoStep(generator, operators, processors, requestInfo, newGenerate=True):
    if newGenerate:
        request = generator.UpdateTime(timeStep)
        if request:
            requestInfo['generated'] += 1
            operatorIndex = ChooseOperator(operators)
            if operatorIndex == -1: # все операторы заняты
                requestInfo['lost'] += 1
            else:
                operators[operatorIndex].acceptRequest(request)

    for curOperator in operators:
        curOperator.UpdateTime(timeStep)

    for curProcessor in processors:
        res = curProcessor.UpdateTime(timeStep)
        if res == 0:  # заявка была обработана
            requestInfo['processed'] += 1


def modeling(generator, operators, processors, incomingRequestAmount):
    requestInfo = {'generated': 0, 'lost': 0, 'processed': 0}

    while requestInfo['generated'] < incomingRequestAmount:
        DoStep(generator, operators, processors, requestInfo)

    while requestInfo['lost'] + requestInfo['processed'] < incomingRequestAmount:
        DoStep(generator, operators, processors, requestInfo, False)

    return requestInfo


def main():
    clientGenerator = Generator(UniformDistribution(8, 12))

    firstQueue = []
    secondQueue = []

    operators = [
        Operator(firstQueue, UniformDistribution(15, 25)),    
        Operator(firstQueue, UniformDistribution(30, 50)),
        Operator(secondQueue, UniformDistribution(20, 60))    
    ]

    processors = [
        Processor(firstQueue, UniformDistribution(15, 15)),   
        Processor(secondQueue, UniformDistribution(30, 30))   
    ]

    totalRequests = 3000

    tStart = time()
    res = modeling(clientGenerator, operators, processors, totalRequests)

    print('time (secs)', time() - tStart)
    for key in res.keys():
        print(key, res[key])

    print('lost', res['lost'] / totalRequests)


if __name__ == '__main__':
    main()
