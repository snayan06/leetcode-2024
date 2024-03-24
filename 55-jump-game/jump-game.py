class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if you can reach the last index of the array using the jump rules.

        Args:
        - nums (List[int]): A list of non-negative integers representing the maximum jump length at each position.

        Returns:
        - bool: True if it is possible to reach the last index, False otherwise.

        Intuition:
        - The idea is to iterate through the array from right to left.
        - Maintain a variable `last_good_index`, which represents the furthest index we can reach from the current position.
        - If we find an index `i` from where we can reach `last_good_index`, update `last_good_index` to `i`.
        - At the end, if `last_good_index` reaches the start of the array (index 0), it means we can jump to the last index.

        Complexity Analysis:
        - Time Complexity: O(n), where n is the length of the input array `nums`.
          The algorithm iterates through the array once.
        - Space Complexity: O(1), as only a constant amount of extra space is used.
        """
        n = len(nums)
        last_good_index = n - 1
        
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= last_good_index:
                last_good_index = i
        
        if last_good_index == 0:
            return True
        
        return False
