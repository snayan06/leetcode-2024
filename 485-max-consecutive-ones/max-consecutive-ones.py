from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Find the maximum number of consecutive 1's in a binary array.

        Intuition:
        - We can use a sliding window approach to traverse the array and count consecutive 1's.
        - Initialize two pointers, `l` (left) and `r` (right), to define the sliding window.
        - Start with `l` and `r` both at the beginning of the array.
        - Move `r` to the right while counting consecutive 1's (`c`) until encountering a 0.
        - When encountering a 0, update the maximum length (`max_len`) if `c` is greater than the current maximum.
        - Reset `c` to 0 and move `l` to `r` to start a new window.
        - Continue until reaching the end of the array.
        - Finally, return the maximum length of consecutive 1's found.

        Time Complexity: O(n)
        - The algorithm traverses the array once from left to right.
        
        Space Complexity: O(1)
        - Constant space is used for variables.
        """
        l, r = 0, 0
        max_len = 0
        c = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
                c += 1
            else:
                max_len = max(c, max_len)
                l = r
                r += 1
                c = 0

        return max(max_len, c)
