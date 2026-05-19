class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        for i, n in enumerate(nums):
            prefix.append(prefix[i] * n)
        
        for i, n in enumerate(reversed(nums)):
            postfix.insert(0, postfix[0] * n)

        result = []
        for i, n in enumerate(nums):
            result.append(prefix[i] * postfix[i + 1])
            
        return result