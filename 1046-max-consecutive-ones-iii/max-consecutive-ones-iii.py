from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Find the length of the longest subarray with at most k zeroes.

        Intuition:
        - We can use a sliding window approach to traverse the array and count zeroes.
        - Initialize two pointers, `l` (left) and `r` (right), to define the sliding window.
        - Start with `l` and `r` both at the beginning of the array.
        - Move `r` to the right while counting zeroes until encountering more than `k` zeroes.
        - When encountering more than `k` zeroes, move `l` to the right until the number of zeroes becomes less than or equal to `k`.
        - Update the answer with the maximum length of the subarray found.
        - Continue until reaching the end of the array.
        - Finally, return the answer.

        Time Complexity: O(n)
        - The algorithm traverses the array once from left to right.

        Space Complexity: O(1)
        - Constant space is used for variables.
        """
        l, r = 0, 0
        zero = 0
        answer = 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            if zero <= k:
                answer = max(answer, r - l + 1)

            r += 1

        return answer
