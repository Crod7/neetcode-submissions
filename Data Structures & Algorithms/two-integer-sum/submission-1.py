class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = {}
        # key = number in nums value = index
        for i, n in enumerate(nums):
            val = target - n

            if val in hashset:
                return [hashset[val], i]
            else:
                hashset[n] = i
