class Processor:
    def __init__(self, requestsQueue, distribution):
        self.timeDistribution = distribution
        self.busy = False
        self.requestsQueue = requestsQueue
        self.finishTime = 0

    def UpdateTime(self, dt):
        self.finishTime -= dt

        if self.busy and self.finishTime <= 1e-5:
            self.busy = False
            self.curRequest = None
            return 0

        if not self.busy and len(self.requestsQueue) != 0:
            self.requestsQueue.pop(0)
            self.finishTime = self.timeDistribution.generate()
            self.busy = True
            return 1

        return 2
