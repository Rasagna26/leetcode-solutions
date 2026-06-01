class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
            
        board = [["."] * n for _ in range(n)]
        res = []

        def isSafe(r, c):
            # check column
            for i in range(r):
                if board[i][c] == "Q":
                    return False

            # left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # right diagonal
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def bt(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    bt(row + 1)
                    board[row][col] = "."   # backtrack

        bt(0)
        return res
