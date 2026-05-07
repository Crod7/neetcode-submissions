class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i = 0

        if len(nums) == 0:
            return nums

        while i <= len(nums) - 1:
            if i == 0:
                i = i + 1
                continue
            if nums[i] >= nums[i - 1]:
                i = i + 1 
                continue
            if nums[i] < nums[i - 1]:
                temp = nums[i]
                nums.pop(i)
                nums.insert(i - 1, temp)
                i = i - 1
                if i == 0:
                    i = 1
                continue
        return nums