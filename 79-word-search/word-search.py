from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Check if the given word can be formed by a sequence of adjacent characters in the board.
        
        Intuition:
        - We perform a depth-first search (DFS) starting from each cell in the board that matches the first letter of the word.
        - During the DFS traversal, we explore neighboring cells recursively to find subsequent letters of the word.
        - We use a dictionary to map cell coordinates to their values for efficient lookups during DFS.
        - To avoid revisiting the same cell, we mark visited cells by temporarily replacing their values with a placeholder.
        - After exploring neighboring cells, we restore the original value of the cell and backtrack to explore other paths.
        
        Time Complexity: O(M * N * 4^L), where M and N are the dimensions of the board, and L is the length of the word.
        - For each cell in the board, we perform DFS with a branching factor of 4 (up, down, left, right).
        - The worst-case time complexity occurs when the word is not found, and we explore all possible paths in the grid.
        
        Space Complexity: O(M * N + L), where M and N are the dimensions of the board, and L is the length of the word.
        - We use a dictionary to store cell values, which requires O(M * N) space.
        - The recursive DFS call stack can have a depth of at most L, where L is the length of the word.
        - Additional space is used for variables and function call overhead.
        """
        rows, cols = len(board), len(board[0])
        cell_dict = {(i, j): board[i][j] for i in range(rows) for j in range(cols)}
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            if (i, j) not in cell_dict or cell_dict[(i, j)] != word[k]:
                return False
            temp, cell_dict[(i, j)] = cell_dict[(i, j)], '/'
            found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            cell_dict[(i, j)] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
