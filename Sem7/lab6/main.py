from time import time
from UniformDistribution import UniformDistribution
from Generator import Generator
from Operator import Operator
from Attraction import Attraction

timeStep = 0.01

def DoStep(generator, operators, Attractions, visitorInfo, newGenerate=True):
    if newGenerate:
        res = generator.UpdateTime(timeStep)
        if res:       
            visitorInfo['generated'] += 1

    for curOperator in operators:
        curOperator.UpdateTime(timeStep)

    for curAttraction in Attractions:
        res = curAttraction.UpdateTime(timeStep)
        if res == 0:
            visitorInfo['processed'] += 1
        elif res == -1:
            visitorInfo['lost'] += 1
            
def modeling(generator, operators, Attractions, incomingVisitorAmount):
    visitorInfo = {'generated': 0, 'lost': 0, 'processed': 0}

    while visitorInfo['generated'] < incomingVisitorAmount:
        DoStep(generator, operators, Attractions, visitorInfo)

    while visitorInfo['processed'] < incomingVisitorAmount:
        DoStep(generator, operators, Attractions, visitorInfo, False)

    return visitorInfo


def main():
    firstQueueGroup = [[], [], []]
    secondQueueGroup = [[], []]

    clientGenerator = Generator(UniformDistribution(1, 5), firstQueueGroup)

    operators = [
        Operator(firstQueueGroup[0], secondQueueGroup, UniformDistribution(2, 5)),    
        Operator(firstQueueGroup[1], secondQueueGroup, UniformDistribution(4, 8)),
        Operator(firstQueueGroup[2], secondQueueGroup, UniformDistribution(10, 15))    
    ]

    Attractions = [
        Attraction(secondQueueGroup[0], UniformDistribution(5, 9)),   
        Attraction(secondQueueGroup[1], UniformDistribution(10, 25))   
    ]

    totalVisitors = 300

    tStart = time()
    res = modeling(clientGenerator, operators, Attractions, totalVisitors)

    print('time (secs)', time() - tStart)
    for key in res.keys():
        print(key, res[key])

    print('lost', res['lost'] / totalVisitors)


if __name__ == '__main__':
    main()
