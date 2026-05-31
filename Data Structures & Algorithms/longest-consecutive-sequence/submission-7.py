class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 1
        # if len(nums) == 0:
        #     return 0

        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        res = 0
        maxResult = 0
        curr = 0
        firstRun = 0
        while hashmap:       
            if firstRun == 0:
                firstRun = 1
                res = 1
                maxResult = max(maxResult, res)
                curr = min(hashmap)
                hashmap.pop(curr) 
                continue
            
            if curr + 1 == min(hashmap):
                if res == 0:
                    res = 1
                res += 1
                maxResult = max(maxResult, res)
            else:
                res = 0

            curr = min(hashmap)
            hashmap.pop(curr) 

        return maxResult
