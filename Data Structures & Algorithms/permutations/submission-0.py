class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result= []

        def dfs(subset, choices):
            if len(choices) == 0:
                result.append(subset.copy())
                return

            for i, n in enumerate(choices):
                subset.append(n)
                choices.pop(i)
                dfs(subset, choices)
                choices.insert(i, n)
                subset.pop()
        
        dfs([], nums)

        return result