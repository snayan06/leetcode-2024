from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        R: int = len(matrix)
        C: int = len(matrix[0])
        min_rows: List[float] = [float('inf')] * R
        max_columns: List[float] = [-float('inf')] * C

        for row in range(R):
            for col in range(C):
                if matrix[row][col] < min_rows[row]:
                    min_rows[row] = matrix[row][col]

        # Calculate the maximum value in each column
        for col in range(C):
            for row in range(R):
                if matrix[row][col] > max_columns[col]:
                    max_columns[col] = matrix[row][col]

        answer: List[int] = []

        # Check for each element if it is the minimum in its row and the maximum in its column
        for row in range(R):
            for col in range(C):
                if matrix[row][col] == min_rows[row] == max_columns[col]:
                    answer.append(matrix[row][col])

        return answer