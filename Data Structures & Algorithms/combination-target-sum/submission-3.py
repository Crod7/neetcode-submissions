class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, i, total):

            if i > len(nums) - 1:
                return
            if total > target:
                return

            if total == target:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(subset, i, total + nums[i])
            subset.pop()

            dfs(subset, i + 1, total)

        dfs([], 0, 0)

        return res