class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stoneA = stones.pop()
            stoneB = stones.pop()
            leftOver = stoneA - stoneB
            if leftOver > 0:
                stones.append(leftOver)
            stones.sort()
        
        if len(stones) == 0:
            return 0
            
        return stones[0]