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
        - O(n + k*log(n)), where n is the number of unique elements in the list.
          O(n) for counting occurrences using a hash map (dictionary),
          O(k*log(n)) for sorting the unique elements based on frequency.

        Space Complexity:
        - O(n), where n is the number of unique elements in the list.
          The hash map stores the count of each unique element.
        """
        hash_map = {}
        
        # Count occurrences of each element in the list
        for num in nums:
            c = hash_map.get(num, 0)
            hash_map[num] = c + 1
        
        # Sort the hash map based on frequency in descending order
        sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        
        return list(sorted_dict.keys())[:k]
