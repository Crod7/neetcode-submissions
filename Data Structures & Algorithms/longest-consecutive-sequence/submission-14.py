class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        minHeap = []
        for n in nums:
            minHeap.append(n)

        heapq.heapify(minHeap)
        res = 1
        temp = 1

        currNum = heapq.heappop(minHeap)

        while minHeap:
            nextNum = heapq.heappop(minHeap)
            if nextNum == currNum:
                continue

            if nextNum == currNum + 1:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1
            
            currNum = nextNum
        
        return res

            

