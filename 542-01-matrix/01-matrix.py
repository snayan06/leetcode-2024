from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # thinking level order traversal with all the nodes ... multisource BFS problem ...
        # In the Rotten Oranges problem, you start BFS from all initially rotten oranges to spread the rot to fresh oranges.
        # Similarly, in the 01 Matrix problem, you start BFS from all 0s to spread the known shortest distance to 0 to all 1s.

        R = len(mat)
        C = len(mat[0])
        dist = [[C * R + 1] * C for _ in range(R)]
        queue = deque()
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    dist[i][j] = 0
        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    # If the new distance is shorter, update and enqueue the cell
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
        return dist
