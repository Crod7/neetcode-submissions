class MedianFinder:
    

    def __init__(self):
        self.sm = [] # -3,-2,-1 pop gets us (3)
        self.lg = [] # 1,2,3    pop gets us (1)

    def addNum(self, num: int) -> None:
        if self.lg and num > self.lg[0]:
            heapq.heappush(self.lg, num)
        else:
            heapq.heappush(self.sm, -num)

        if len(self.sm) > len(self.lg) + 1:
            heapq.heappush(self.lg, -(heapq.heappop(self.sm)))
        elif len(self.sm) + 1 < len(self.lg):
            heapq.heappush(self.sm, -(heapq.heappop(self.lg)))

    def findMedian(self) -> float:
        if len(self.sm) > len(self.lg):
            return -(self.sm[0])
        elif len(self.sm) < len(self.lg):
            return (self.lg[0])
        else:
            return (-(self.sm[0]) + (self.lg[0])) / 2

