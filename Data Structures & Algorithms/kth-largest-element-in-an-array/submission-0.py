class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxNums = [-n for n in nums]

        heapq.heapify(maxNums)
        res = []
        
        while k > 0:
            val = heapq.heappop(maxNums)
            k -= 1
            if k == 0:
                res.append(-val)

        return res[0]