class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i <= len(nums) - 1:
            if i == 0:
                i = i + 1
                continue
            if nums[i] >= nums[i-1]:
                i = i + 1
                continue
            if nums[i] < nums[i-1]:
                temp = nums.pop(i)
                nums.insert(i-1, temp)
                i = i - 1
                continue
        