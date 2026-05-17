class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create prefix array by appending to it
        prefix = [1]
        for i, n in enumerate(nums):
            prefix.append( prefix[i] * n )
        # Create Postfix array by inserting into at 0 index
        postfix = [1]
        for n in reversed(nums):
            postfix.insert(0, postfix[0] * n)
        # create temp array
        result = []
        for i, n in enumerate(nums):
            result.append(prefix[i] * postfix[i + 1])

        return result 


