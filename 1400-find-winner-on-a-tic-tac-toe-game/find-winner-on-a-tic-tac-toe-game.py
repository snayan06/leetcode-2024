class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * 3, [0] * 3
        diag1 = 0
        diag2 = 0
        index = 0
        for move in moves:
            i, j = move
            sign = 0
            if index % 2 == 0:
                sign = 1
            else:
                sign = -1
            rows[i] += sign
            cols[j] += sign
            if i == j:
                diag1 += sign
            if i + j == n - 1:
                diag2 += sign
            print(rows[i], cols[j], diag1, diag2)
            if (
                abs(rows[i]) == n
                or abs(cols[j]) == n
                or abs(diag1) == n
                or abs(diag2) == n
            ):
                if sign == 1:
                    return "A"
                else:
                    return "B"
            index += 1
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
