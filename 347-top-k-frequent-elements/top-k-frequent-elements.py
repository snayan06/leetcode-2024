from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find the k most frequent elements in the given list of integers.

        Args:
        - nums (List[int]): The list of integers.
        - k (int): The number of most frequent elements to return.

        Returns:
        - List[int]: The k most frequent elements in the list.

        Time Complexity:
        - Approach 1: O(n + k*log(n)), where n is the number of unique elements in the list.
          O(n) for counting occurrences using a hash map (dictionary),
          O(k*log(n)) for sorting the unique elements based on frequency.

        - Approach 2: O(n + k*log(n)), where n is the number of unique elements in the list.
          O(n) for counting occurrences using a hash map (dictionary),
          O(k*log(n)) for maintaining a max heap of size k.

        - Approach 3: O(n), where n is the number of unique elements in the list.
          O(n) for counting occurrences using a hash map (dictionary),
          O(n) for creating buckets and inserting elements based on frequency.

        Space Complexity:
        - O(n), where n is the number of unique elements in the list.
          The hash map stores the count of each unique element.
        """
        hash_map = {}
        
        # Count occurrences of each element in the list
        for num in nums:
            c = hash_map.get(num, 0)
            hash_map[num] = c + 1

        # Approach 1: Sort the hash map based on frequency in descending order
        # sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        # Approach 2: Use a max heap to keep track of the top k frequent elements
        # max_heap = [(-count, num) for num, count in hash_map.items()]
        # heapq.heapify(max_heap)
        # result_heap = [heapq.heappop(max_heap)[1] for _ in range(k)]

        # Approach 3: Bucket Sort
        buckets = [None] * (len(nums) + 1)
        for num, count in hash_map.items():
            if buckets[count] is None:
                buckets[count] = []
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i] is not None:
                result.extend(buckets[i])
                if len(result) >= k:
                    break

        return result[:k]
