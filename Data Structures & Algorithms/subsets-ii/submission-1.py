class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list1 = []
        set1 = set()
        nums.sort()

        def dfs(i, subset):
            
            list1.append(subset.copy())
            if i >= len(nums):
                 return

            
            
            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            dfs(i + 1, subset)
        

        dfs(0, [])

        for li in list1:
            set1.add(tuple(li))

        result = [list(t) for t in set1]
        return result


