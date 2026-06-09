class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])

                if board[i][j] in squares[i // 3, j //3]:
                    return False
                else:
                    squares[i // 3, j //3].add(board[i][j])

        return True

