class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)     # 0,1,2,3,4,...
        cols = collections.defaultdict(set)     # 0,1,2,3,4,...
        squares = collections.defaultdict(set)  # (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] 
                or board[r][c] in cols[c] 
                or board[r][c] in squares[r//3, c//3]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r // 3, c // 3].add(board[r][c])
                
        return True
