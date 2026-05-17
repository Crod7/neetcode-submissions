class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Edge case, if len <= 1 return nums
        if len(nums) <= 1:
            return nums

        # make temp prefix array [1,1,2,8,]
        prefix = [1]
        for i, n in enumerate(nums):
            prefix.append(prefix[i] * n)

        # make temp postfix array
        postfix = [1]
        for i, n in enumerate(reversed(nums)):
            postfix.insert(0, postfix[0] * n)

        # recreate the nums array
        result = []
        for i, n in enumerate(nums):
            result.append(prefix[i] * postfix[i + 1])


        return result