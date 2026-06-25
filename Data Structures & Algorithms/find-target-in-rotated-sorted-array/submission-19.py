class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] > nums[m]:
                if nums[r] < target or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # 1,2,3,4,5,6
                if nums[l] > target or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1



        return -1
            
