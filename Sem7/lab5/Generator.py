class Generator:
    def __init__(self, distribution):
        self.timeDistribution = distribution
        self.finishTime = 0
        self.requestId = -1

    def UpdateTime(self, dt):
        self.finishTime -= dt

        if self.finishTime <= 1e-5:
            self.finishTime = self.timeDistribution.generate()
            self.requestId += 1
            return self.requestId

        return None
