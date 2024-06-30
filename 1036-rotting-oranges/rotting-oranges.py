from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        This function solves the problem of determining the minimum number of minutes that must elapse until no cell
        has a fresh orange. If it is impossible to rot all fresh oranges, the function returns -1. The approach used
        here is based on multi-source Breadth-First Search (BFS).

        Detailed Intuition and Approach:

        1. **Multi-source BFS Initialization**:
           - We start by identifying all the initially rotten oranges in the grid.
           - These rotten oranges will serve as the starting points (sources) for our BFS traversal.
           - We use a queue to facilitate the BFS process, as it allows us to process each level of oranges minute by minute.
           - Additionally, a set is used to keep track of the positions of discovered (visited) oranges to avoid re-processing.

        2. **Edge Case - Only Empty Cells**:
           - Before proceeding, we check if the grid contains only empty cells (0s).
           - If the grid has only empty cells, there are no oranges to process, so we return 0 immediately.

        3. **Queue Initialization**:
           - We iterate through the grid to find all initially rotten oranges (cells with value 2).
           - Each rotten orange's position is added to the queue and the discovered set.
           - If there are no rotten oranges but the grid contains fresh oranges, it's impossible to rot any fresh oranges, so we return -1.

        4. **Directional Movement**:
           - For BFS traversal, we define four possible directions (up, down, left, right) to move from each cell.

        5. **BFS Traversal**:
           - We process each level of the BFS, representing each minute that passes.
           - For each rotten orange, we check its four neighboring cells.
           - If a neighboring cell contains a fresh orange (value 1), we mark it as rotten (set value to 2), add its position to the queue, and to the discovered set.
           - Once all cells at the current level are processed, we increment the minute counter if there are more oranges to process.

        6. **Completion Check**:
           - After completing the BFS traversal, we perform a final scan of the grid to check for any remaining fresh oranges.
           - If any fresh oranges are found, it means not all oranges could be rotted, and we return -1.
           - If no fresh oranges remain, we return the total minutes elapsed.

        Parameters:
        grid (List[List[int]]): The 2D grid representing the box of oranges where
                                0 = empty cell, 1 = fresh orange, 2 = rotten orange.

        Returns:
        int: The minimum number of minutes required to rot all fresh oranges, or -1 if impossible.
        """

        # Initialize the queue and discovered set
        queue = Queue()
        discovered = set()
        m = len(grid)
        n = len(grid[0])

        # Check if the grid contains only empty cells
        only_empty = True

        # Enqueue all initial rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.put((i, j))
                    discovered.add((i, j))
                if grid[i][j] != 0:
                    only_empty = False

        print(discovered)

        # If the grid contains only empty cells, return 0
        if only_empty:
            return 0

        # If there are no rotten oranges and the grid contains fresh oranges, return -1
        if queue.empty():
            return -1

        answer = 0
        # Four directions we can go
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # up  # left  # down  # right

        while not queue.empty():
            size = queue.qsize()
            # Process all the nodes which are rotten (multi-source BFS)
            for _ in range(size):
                curr_x, curr_y = queue.get()
                print("Processing:", curr_x, curr_y)

                for dx, dy in directions:
                    new_x, new_y = curr_x + dx, curr_y + dy

                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        queue.put((new_x, new_y))
                        discovered.add((new_x, new_y))

            # One level is done but as queue is not empty we have to keep going hence addition of minute
            if not queue.empty():
                answer += 1

        # After this whole traversal, if still some oranges are fresh then
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return answer
