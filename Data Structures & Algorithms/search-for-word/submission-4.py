class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        path = set() # (row, col)

        def dfs(r, c, i): # word[i]
            if i == len(word):
                return True

            if (r >= rows or c >= cols or r < 0 or c < 0 or (r,c) in path or word[i] != board[r][c]):
                return False
            
            path.add((r,c))

            res = (dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1) or dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1))

            path.remove((r,c))

            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c,0):
                    return True
        return False
            
