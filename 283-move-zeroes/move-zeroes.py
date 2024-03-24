class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Modify the input list in-place by moving all zeros to the end.

        Args:
        - nums (List[int]): The input list of integers.

        Returns:
        - None

        Intuition:
        - Use a two-pointer approach where the left pointer keeps track of the position to insert non-zero elements.
          When a non-zero element is encountered, it is swapped with the element at the left pointer, effectively
          moving it towards the beginning of the list.

        Time Complexity:
        - O(n), where n is the length of the input list. We traverse the list once.

        Space Complexity:
        - O(1), constant space is used for variables.
        """
        # Initialize the left pointer to 0
        left = 0

        # Iterate through the list with the right pointer
        for right in range(len(nums)):
            # If the current element is non-zero
            if nums[right] != 0:
                # Swap the non-zero element with the element at the left pointer
                nums[right], nums[left] = nums[left], nums[right]
                # Increment the left pointer to move to the next position
                left += 1
