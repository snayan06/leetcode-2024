from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        answer = 0
        visited = [False] * n

        def dfs(node):
            for neighbour in range(n):  # Corrected syntax here
                if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)

        for city in range(n):  # Corrected iteration over range
            if not visited[city]:
                visited[city] = True  # Mark the city as visited
                dfs(city)
                answer += 1

        return answer
