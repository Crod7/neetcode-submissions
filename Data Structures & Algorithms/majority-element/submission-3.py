class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        result = 0
        currentKey = 0

        # change to grab value, not key
        for key, value in hashmap.items():
            if value > result:
                result = value
                currentKey = key

        
        return currentKey 