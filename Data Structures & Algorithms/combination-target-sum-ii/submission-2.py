class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        
        def dfs(i, total, curr):
            if total == target:
                res.add(tuple(curr))
                return
            
            if total > target or i > len(candidates) - 1:
                return
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i], curr)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr.pop()
            dfs(i + 1, total, curr)
        dfs(0, 0, [])
        
        return [list(item) for item in res]