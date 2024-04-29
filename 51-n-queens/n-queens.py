from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Intuition:
            This solution uses backtracking to place queens on the chessboard. We recursively explore all possible
            placements of queens, ensuring that no two queens threaten each other. At each step, we check whether
            it's safe to place a queen in the current position. If it is safe, we place the queen and move to the
            next column. If not, we backtrack and try a different position.

        Time Complexity:
            The time complexity of this solution is O(N!), where N is the size of the chessboard. This is because
            we explore all possible combinations of queen placements, which grows factorially with the size of the
            chessboard.

        Space Complexity:
            The space complexity of this solution is O(N^2) to store the chessboard and the list of solutions.
        """

        ans = []

        def isSafe(row, col, board):

            # Check diagonal and column conflicts
            duprow = row
            dupcol = col

            # Check upper-left diagonal
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            # Reset row and col
            row = duprow
            col = dupcol

            # Check left
            while col >= 0:
                if board[row][col] == "Q":
                    return False
                col -= 1

            # Reset row and col
            row = duprow
            col = dupcol

            # Check lower-left diagonal
            while col >= 0 and row < n:
                if board[row][col] == "Q":
                    return False
                col -= 1
                row += 1

            return True

        def helperFunc(board, col):

            # base case
            if col == n:
                ans.append(list(board))
                return

            # Recursively try placing a queen in each row of the current column
            for ind in range(n):
                if isSafe(ind, col, board):
                    # Choose
                    board[ind] = board[ind][:col] + "Q" + board[ind][col + 1 :]
                    helperFunc(board, col + 1)
                    # Backtrack / unchoose
                    board[ind] = board[ind][:col] + "." + board[ind][col + 1 :]

        # board creation
        board = []
        for _ in range(n):
            s = ""
            for _ in range(n):
                s += "."
            board.append(s)

        helperFunc(board, 0)

        return ans
