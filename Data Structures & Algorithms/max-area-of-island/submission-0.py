class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        r, c, rows, cols = 0, 0, len(grid), len(grid[0])

        def dfs(r,c):
            area = 0
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return area
            
            if grid[r][c] == 1:
                area += 1
            
            grid[r][c] = 0

            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)
            
            
            return area




        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r, c))
                
        return maxArea