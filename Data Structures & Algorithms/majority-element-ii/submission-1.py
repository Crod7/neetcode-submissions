class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        res = []
        for key, value in hashmap.items():
            if value > math.floor(len(nums)/ 3 ):
                res.append(key)

        return res