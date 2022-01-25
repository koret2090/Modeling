class Operator:
    def __init__(self, queue, queueGroup, distribution):
        self.timeDistribution = distribution
        self.busy = False
        self.queue = queue
        self.queues = queueGroup
        self.curVisitor = None
        self.finishTime = 0

    def acceptVisitor(self):
        self.busy = True
        self.curVisitor = self.queue.pop(0)
        self.finishTime = self.timeDistribution.generate()

    def finishCurVisitor(self):
        self.AddToQueue()
        self.busy = False
        self.curVisitor = None

    def AddToQueue(self):
        minLen = len(self.queues[0])
        minQueueIndex = 0
        for i in range(1, len(self.queues)):
            if len(self.queues[i]) < minLen:
                minLen = len(self.queues[i])
                minQueueIndex = i
        self.queues[minQueueIndex].append(self.curVisitor)

    def UpdateTime(self, dt):
        self.finishTime -= dt
        if not self.busy and len(self.queue) > 0:
            self.acceptVisitor()

        if self.busy and self.finishTime <= 1e-5:
            self.finishCurVisitor()
            return 0
        return 2

    
