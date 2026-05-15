class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pre = [1]
        post = [1]

        for i,n in enumerate(nums):
            #
            pre.append(pre[i] * n)
        
        for n in reversed(nums):
            #
            post.insert(0, post[0] * n)

        result = []
        for i,n in enumerate(nums):
            #
            result.append(pre[i] * post[i + 1])
        return result
