from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search for a target value in a 2D matrix sorted in ascending order both horizontally and vertically.

        Args:
            matrix (List[List[int]]): The input 2D matrix.
            target (int): The target value to search for.

        Returns:
            bool: True if the target is found in the matrix, False otherwise.

        Intuition:
            The main intuition behind this algorithm is to treat the 2D matrix as a flattened 1D array,
            allowing us to perform binary search efficiently. To achieve this, we calculate the row and
            column of the middle element using the formula: 
                row = mid // cols
                col = mid % cols
            where 'mid' is the index of the middle element in the flattened array, 'cols' is the number of
            columns in the matrix. By doing this, we effectively map the 1D index 'mid' to its corresponding
            2D indices (row, col) in the original matrix.

            Additionally, to determine the total size of the matrix, we calculate it as 'rows * cols', where
            'rows' is the number of rows and 'cols' is the number of columns in the matrix. This helps us in
            defining the boundaries for binary search.

        Time complexity:
            The time complexity of this algorithm is O(log(m*n)), where 'm' is the number of rows in the matrix
            and 'n' is the number of columns. This complexity arises because we are performing binary search
            on a flattened version of the matrix, which has 'm*n' elements.
        """

        # Determine the number of rows and columns in the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize pointers for binary search
        left, right = 0, rows * cols - 1

        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            # Calculate the row and column of the middle element
            row = mid // cols
            col = mid % cols
            # Get the value of the middle element
            element = matrix[row][col]

            if target == element:
                return True
            elif target < element:
                right = mid - 1
            else:
                left = mid + 1

        # If the target is not found, return False
        return False
