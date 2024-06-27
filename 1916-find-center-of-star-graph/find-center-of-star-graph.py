class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Extract nodes from the first edge
        u1, v1 = edges[0]
    # Extract nodes from the second edge
        u2, v2 = edges[1]

        # The node that appears in both edges is the center
        if u1 == u2 or u1 == v2:
            return u1
        else:
            return v1
        