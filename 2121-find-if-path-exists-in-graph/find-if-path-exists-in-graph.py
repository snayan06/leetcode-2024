class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.build_graph(edges)
        visited = [False] * n
        print(graph)
        def dfs(node):
            if node == destination:
                return True  # Found a path!

            visited[node] = True  # Mark the current node as visited

            for neighbor in graph[node]:
                if not visited[neighbor]:  # Explore only unvisited neighbors
                    if dfs(neighbor):  # Recursion
                        return True

            return False  # No path found from this node (backtracking)

        return dfs(source)  # Start the search from the source node

    def build_graph(self, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # For undirected graphs
        return graph
