class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]

        for i, n in enumerate(nums):
            pre.append(n * pre[-1])
        for n in reversed(nums):
            post.insert(0, n * post[0])
        
        result = []
        for i in range(len(nums)):
            result.append(pre[i] * post[i + 1])

        return result