class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[r]

        while l <= r:
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[l] > nums[m]:
                if nums[l] < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return res