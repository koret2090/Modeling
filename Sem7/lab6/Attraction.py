from random import random
class Attraction:
    def __init__(self, visitorsQueue, distribution):
        self.timeDistribution = distribution
        self.busy = False
        self.visitorsQueue = visitorsQueue
        self.finishTime = 0

    def UpdateTime(self, dt):
        self.finishTime -= dt
        if self.busy and self.finishTime <= 1e-5:
            self.busy = False
            return 0

        if not self.busy and len(self.visitorsQueue) != 0:
            if random() < 0.75:
                self.visitorsQueue.pop(0)
                self.finishTime = self.timeDistribution.generate()
                self.busy = True
                return 1
            else:
                return -1

        return 2
