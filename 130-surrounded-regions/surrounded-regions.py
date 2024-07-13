class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board and not board[0]:
            return
        R = len(board)
        C = len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(sr, sc):
            board[sr][sc] = "E"
            for dx, dy in directions:
                new_sr, new_sc = sr + dx, sc + dy
                if 0 <= new_sr < R and 0 <= new_sc < C and board[new_sr][new_sc] == "O":
                    dfs(new_sr, new_sc)

        # mark all boarders 'O'

        for i in range(R):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][C - 1] == "O":
                dfs(i, C - 1)

        for j in range(C):
            if board[0][j] == "O":
                dfs(0, j)
            if board[R - 1][j] == "O":
                dfs(R - 1, j)

        # Step 2: Flip all remaining 'O's to 'X' and restore 'E's back to 'O'
        for row in range(R):
            for col in range(C):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "E":
                    board[row][col] = "O"

        return
