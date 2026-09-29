class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r, c, LandHo):
            if r < 0 or c < 0 or r >= rows or c >= cols or tuple([r,c]) in visited:
                return

            visited.add(tuple([r,c]))
            if grid[r][c] == "0":
                return
            
            dfs(r - 1, c, False)
            dfs(r + 1, c, False)
            dfs(r, c - 1, False)
            dfs(r, c + 1, False)

        
        for r in range(rows):
            for c in range(cols):
                if tuple([r,c]) not in visited and grid[r][c] == "1":
                    res += 1
                dfs(r, c, True)
        print(visited)
        return res