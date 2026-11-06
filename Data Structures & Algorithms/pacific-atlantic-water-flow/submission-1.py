class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        result = []

        pac = set()
        atl = set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or prevHeight > heights[r][c]):
                return    
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for r in range(rows):
            for c in range(cols):
                if c == 0 or r == 0:
                    dfs(r,c,pac,heights[r][c])
                if c == cols - 1 or r == rows - 1:
                    dfs(r,c,atl,heights[r][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result
        
        


