class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        cell_dict = {}
        for i in range(rows):
            for j in range(columns):
                cell_dict[(i, j)] = board[i][j]

        def dfs(i, j, k):
            if len(word) == k:
                return True

            if (i, j) not in cell_dict or cell_dict[(i, j)] != word[k]:
                return False

            temp, cell_dict[(i, j)] = cell_dict[(i, j)], "/"
            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )
            cell_dict[(i, j)] = temp
            return found

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
