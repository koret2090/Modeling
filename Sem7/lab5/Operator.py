class Operator:
    def __init__(self, queue, distribution):
        self.timeDistribution = distribution
        self.busy = False
        self.queue = queue
        self.curRequest = None
        self.finishTime = 0

    def acceptRequest(self, request):
        self.busy = True
        self.curRequest = request
        self.finishTime = self.timeDistribution.generate()

    def finishCurRequest(self):
        self.queue.append(self.curRequest)
        self.busy = False
        self.curRequest = None

    def UpdateTime(self, dt):
        self.finishTime -= dt
        if self.busy and self.finishTime <= 1e-5:
            self.finishCurRequest()
            return 0
        return 2
