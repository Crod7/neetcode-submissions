class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stoneA = heapq.heappop(stones)
            stoneB = heapq.heappop(stones)

            val = abs(stoneA) - abs(stoneB)

            if val != 0:
                heapq.heappush(stones, -val)
        
        stones.append(0)
        return -stones[0]

