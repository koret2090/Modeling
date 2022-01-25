class Generator:
    def __init__(self, distribution, queueGroup):
        self.timeDistribution = distribution
        self.queues = queueGroup
        self.finishTime = 0
        self.visitorId = -1

    def UpdateTime(self, dt):
        self.finishTime -= dt

        if self.finishTime <= 1e-5:
            self.finishTime = self.timeDistribution.generate()
            self.visitorId += 1
            self.AddToQueue()
            return True

        return False

    def AddToQueue(self):
        minLen = len(self.queues[0])
        minQueueIndex = 0
        for i in range(1, len(self.queues)):
            if len(self.queues[i]) < minLen:
                minLen = len(self.queues[i])
                minQueueIndex = i
        self.queues[minQueueIndex].append(self.visitorId)
