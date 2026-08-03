class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        for n in nums:
            prefix.append(prefix[-1] * n)
        
        for n in reversed(nums):
            postfix.insert(0, postfix[0] * n)

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i + 1])
        
        return res
