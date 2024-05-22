class Solution:
    def distance_from_origin(self, x, y):
        return x * x + y * y

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # k smallest => max-heap
        max_heap = []

        for point in points[:k]:
            distance = self.distance_from_origin(point[0], point[1])
            max_heap.append((-distance, point))

        heapq.heapify(max_heap)
        print()

        for point in points[k:]:
            distance = self.distance_from_origin(point[0], point[1])
            if distance < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, point))

        answer = []
        for _, point in max_heap:
            answer.append(point)

        return answer
