class MinStack:

    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:
        self.array.append(val)

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        if self.array:
            currMin = self.array[0]
            for n in self.array:
                temp = n
                if n < currMin:
                    currMin = n
            return currMin
        else:
            return None