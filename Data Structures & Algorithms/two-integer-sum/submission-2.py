class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # number, index

        for i, n in enumerate(nums):
            val = target - n

            if val in hashmap:
                return [hashmap[val], i]
            else:
                hashmap[n] = i
        