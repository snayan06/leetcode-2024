from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum area of water that can be trapped between vertical lines given by heights.

        Intuition:
        The problem is to find the maximum area of water that can be trapped between two vertical lines.
        The area formed between the lines will always be limited by the height of the shorter line and the distance between the lines.
        The wider the gap between the lines and the taller the lines, the more water can be trapped.

        Approach:
        1. Initialize two pointers, left and right, pointing to the start and end of the array respectively.
        2. Calculate the area between the lines using the formula: area = (right - left) * min(height[right], height[left]).
        3. Update the maximum area encountered so far.
        4. Move the pointer with the smaller height towards the other pointer.
        5. Repeat steps 2-4 until the pointers meet.

        Time Complexity:
        The two-pointer approach iterates through the array once, which takes O(n) time.

        Space Complexity:
        The space complexity is O(1) as we are using only a constant amount of extra space.

        Args:
        height (List[int]): List of non-negative integers representing the height of each vertical line.

        Returns:
        int: Maximum area of water that can be trapped.
        """
        n = len(height)
        left, right = 0, n - 1
        area = -1
        while left < right:
            area = max(area, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area
