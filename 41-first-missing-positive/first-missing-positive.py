class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Finds the smallest missing positive integer in an unsorted array.

        Intuition:
        * Leverages cycle sort to rearrange elements within the range [1, n] to their 
          correct indices (i.e., nums[i] = i + 1, if possible).
        * After sorting, the first missing positive is the index + 1 where the 
          array doesn't match this pattern.

        Approach:
        1. **Cycle Sort:**
           * Iterate through the array.
           * For each element 'num', if it's within the valid range (1 to n) and not
             already at its correct index, swap it with the element at 'correct_idx'
             (calculated as num - 1).

        2. **Find Missing Positive:**
           * Iterate through the partially sorted array.
           * If nums[i] != i + 1, the value 'i + 1' is the smallest missing positive.

        3. **All Present:**
           * If the array is completely sorted (all elements 1 to n are in place), 
             the smallest missing positive is n + 1.

        Time Complexity: O(n) due to linear iterations.
        Space Complexity: O(1) as we modify the array in-place.

        Args:
            nums: A list of integers, potentially including duplicates and out-of-range elements.

        Returns:
            The smallest missing positive integer.
        """

        n = len(nums)

        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1 
