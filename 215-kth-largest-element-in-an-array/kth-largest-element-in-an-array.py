import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the k-th largest element in an unsorted list.
        
        Intuition:
        - Use a min heap to keep track of the k largest elements seen so far.
        - Initialize the heap with the first k elements of the list.
        - For each of the remaining elements in the list, if the element is larger than the 
          smallest element in the heap (root of the heap), remove the smallest element and 
          add the new element to the heap.
        - The root of the heap will be the k-th largest element after processing all elements.
        
        Time Complexity: 
        - Building the initial heap with k elements takes O(k) time.
        - Inserting the remaining n-k elements into the heap takes O((n-k) log k) time, 
          as each insertion and deletion operation in the heap takes O(log k) time.
        - Overall, the time complexity is O(n log k).
        
        Space Complexity:
        - The space complexity is O(k) because we maintain a heap with k elements.
        
        Args:
        - nums: List[int] - List of integers.
        - k: int - The order of the largest element to find.
        
        Returns:
        - int: The k-th largest element in the list.
        """
        # Create a min heap for the first k elements
        min_heap = []
        for num in nums[:k]:
            min_heap.append(num)
        
        # Heapify the initial k elements to form a min heap
        heapq.heapify(min_heap)

        # Process the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:  # Compare with the root of the min heap
                heapq.heappop(min_heap)  # Remove the smallest element
                heapq.heappush(min_heap, num)  # Push the new element
        
        # The root of the heap is the k-th largest element
        return min_heap[0]
