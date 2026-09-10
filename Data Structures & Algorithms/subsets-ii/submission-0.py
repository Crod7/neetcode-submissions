class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        setResult = set()

        def dfs(i, subset):
            result.append(subset.copy())
            if i > len(nums) - 1:
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])

        for r in result:
            setResult.add(tuple(r))
        
        #print(setResult)

        my_result = [list(t) for t in setResult]
        return my_result