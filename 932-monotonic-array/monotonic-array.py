class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Check if the given list of integers is monotonic.

        Parameters:
        - nums (List[int]): List of integers to check.

        Returns:
        - bool: True if the list is monotonic (non-decreasing or non-increasing),
                False otherwise.

        Logic:
        - Iterates through the list, setting flags for ascending and descending
          if encountered.
        - Returns True if the list is either entirely non-decreasing or non-increasing.
        """
        asc_flag = False
        dsc_flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dsc_flag = True
            elif nums[i] > nums[i - 1]:
                asc_flag = True
            else:
                pass

        return not (asc_flag and dsc_flag)
