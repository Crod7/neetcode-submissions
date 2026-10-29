class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if board[r][c] != "O":
                return
            
            board[r][c] = "T"
            capture(r - 1, c)
            capture(r + 1, c)
            capture(r, c - 1)
            capture(r, c + 1)

        # capture unsurrounded regions at edges O -> T
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1:
                    capture(r, c)
                if c == 0 or c == cols - 1:
                    capture(r, c)

        # capture surrounded regions double loop O -> X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # uncapture T -> O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"


                    