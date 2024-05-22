import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Find the weight of the last stone remaining after a series of collisions.

        Intuition:
        - Use a max heap to efficiently find the heaviest stones.
        - Simulate the process of smashing the heaviest stones together until no stones are left.
        - Alternatively, the problem could be solved using sorting, but it would have a higher time complexity.

        Time Complexity: O(n * log(n))
        - Building the max heap takes O(n) time, and each heap operation (pop, push) takes O(log(n)) time.
        
        Space Complexity: O(n)
        - The max heap stores all the stones, requiring O(n) space.
        """
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)

        heapq.heapify(max_heap)

        while max_heap and len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -(y - x))
        
        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0