from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        This function solves the problem of finding the minimum number of minutes
        that must elapse until no cell has a fresh orange. If this is impossible,
        it returns -1. The function employs a multi-source BFS approach.

        Intuition:
        1. **Multi-source BFS**: Start from all initially rotten oranges and
           spread the rot level by level. This simulates the passing of minutes.
        2. **Queue Initialization**: All rotten oranges are added to the queue as
           starting points.
        3. **Directional Movement**: From each rotten orange, attempt to rot its
           adjacent fresh oranges (up, down, left, right).
        4. **Time Tracking**: Each level of BFS corresponds to one minute elapsed.
        5. **Termination and Checking**: After the BFS completes, check if any
           fresh oranges remain. If any do, return -1, indicating it's impossible
           to rot all oranges.

        Parameters:
        grid (List[List[int]]): The 2D grid representing the box of oranges where
                                0 = empty cell, 1 = fresh orange, 2 = rotten orange.

        Returns:
        int: The minimum number of minutes required to rot all fresh oranges, or -1 if impossible.
        """

        # First we will have to find all the rotten oranges and put them in a Queue
        queue = Queue()
        discovered = set()
        m = len(grid)
        n = len(grid[0])
        only_empty = True
        # Enqueue all initial rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.put((i, j))
                    discovered.add((i, j))
                if grid[i][j] != 0:
                    only_empty = False
        if only_empty:
            return 0
        # If there are no rotten oranges, return -1
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
