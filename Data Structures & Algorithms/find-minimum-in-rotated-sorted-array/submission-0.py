class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = 0
        while l <= r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = r - 1
            elif nums[m] > nums[r]:
                l = l + 1
            elif l == r: 
                return nums[m]
        return nums[m]