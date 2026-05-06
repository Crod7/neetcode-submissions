class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for item in nums:
            if item in my_set:
                return True
            my_set.add(item)
        return False