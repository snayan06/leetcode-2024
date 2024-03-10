from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        Determine the winner or status of a Tic-Tac-Toe game based on the moves made.

        Args:
        - moves (List[List[int]]): List of moves, where each move is represented as [row, col].

        Returns:
        - str: "A" if player A wins, "B" if player B wins, "Draw" if the game is a draw,
               or "Pending" if the game is still ongoing.

        Intuition:
        - The solution keeps track of the cumulative score for each row, column, and diagonal.
        - Players are represented by signs (1 for player A and -1 for player B).
        - The cumulative score is checked after each move to determine the winner or game status.

        Time Complexity:
        - O(n), where n is the number of moves made. The algorithm iterates over the moves.

        Space Complexity:
        - O(1), constant space is used to store row, column, and diagonal scores.
        """
        n = 3
        # Initialize scores for rows, columns, and diagonals
        rows, cols = [0] * n, [0] * n
        diag1, diag2 = 0, 0
        index = 0  # Variable to track the current move index

        for move in moves:
            i, j = move
            sign = 0

            # Determine the sign based on the player (1 for A, -1 for B)
            if index % 2 == 0:
                sign = 1
            else:
                sign = -1

            # Update scores for the corresponding row, column, and diagonals
            rows[i] += sign
            cols[j] += sign
            if i == j:
                diag1 += sign
            if i + j == n - 1:
                diag2 += sign

            print(rows[i], cols[j], diag1, diag2)

            # Check for a winner after each move
            if (
                abs(rows[i]) == n
                or abs(cols[j]) == n
                or abs(diag1) == n
                or abs(diag2) == n
            ):
                # Return the winner (A or B) based on the sign
                if sign == 1:
                    return "A"
                else:
                    return "B"

            index += 1  # Move to the next index

        # Check for a draw or pending status
        if len(moves) == n*n:
            return "Draw"
        else:
            return "Pending"


