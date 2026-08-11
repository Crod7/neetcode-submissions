class MedianFinder:
    

    def __init__(self):
        self.SmallHeap = [] # +val so we can pull max heap
        self.LargeHeap = [] # val so we can pull min heap



    def addNum(self, num: int) -> None:
        if self.LargeHeap and num > self.LargeHeap[0]:
            heapq.heappush(self.LargeHeap, num)
        else:
            heapq.heappush(self.SmallHeap, -1 * num)

        
        if len(self.SmallHeap) > len(self.LargeHeap) + 1:
            temp = heapq.heappop(self.SmallHeap)
            heapq.heappush(self.LargeHeap, -temp)
        if len(self.LargeHeap) > len(self.SmallHeap) + 1:
            temp = heapq.heappop(self.LargeHeap)
            heapq.heappush(self.SmallHeap, -temp)

    def findMedian(self) -> float:
        if len(self.SmallHeap) > len(self.LargeHeap):
            return -self.SmallHeap[0]
        elif len(self.SmallHeap) < len(self.LargeHeap):
            return self.LargeHeap[0] 
        else:
            return (-self.SmallHeap[0] + self.LargeHeap[0]) / 2
