class MedianFinder:
    

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)
        

    def findMedian(self) -> float:
        self.array.sort()
        if len(self.array) % 2 == 0:
            # even number of items in array
            res = (self.array[(len(self.array)//2)] + self.array[(len(self.array)//2) - 1]) / 2
            return res
        else:
            # off number of items
            return self.array[len(self.array)//2]
        
        