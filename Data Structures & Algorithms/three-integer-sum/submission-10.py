class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, n in enumerate(nums):
            # break since will never be 0 again in an ordered array
            if i > 0 and n == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1  

            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if threesum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                if threesum > 0:
                    r -= 1
                if threesum < 0:
                    l += 1
        return result
                
        