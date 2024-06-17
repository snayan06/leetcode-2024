class Solution:
    def square_root(self, n: int) -> int:
        """
        Calculate the integer square root of a non-negative integer n using binary search.
        
        The function finds the largest integer `mid` such that `mid * mid <= n`.
        It uses binary search to efficiently narrow down the possible values of `mid`.

        Parameters:
        n (int): The number to find the integer square root of.

        Returns:
        int: The largest integer `mid` such that `mid * mid <= n`.
        """
        if n == 0:
            return 0
        l = 0
        r = n
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def judgeSquareSum(self, c: int) -> bool:
        """
        Determine if there exist two integers a and b such that a^2 + b^2 = c.

        The function uses a two-pointer approach:
        1. Calculate the integer square root of c, which serves as the upper bound for b.
        2. Initialize two pointers: left (starting from 0) and right (starting from the integer square root of c).
        3. Iterate and check if the sum of the squares of the pointers equals c.
        4. If the sum is less than c, move the left pointer up to increase the sum.
        5. If the sum is greater than c, move the right pointer down to decrease the sum.
        6. If the sum equals c, return True. If the pointers meet without finding such a pair, return False.

        Parameters:
        c (int): The target sum of the squares of two integers.

        Returns:
        bool: True if there exist two integers a and b such that a^2 + b^2 = c, otherwise False.
        """
        left = 0
        right = self.square_root(c)  # Pass c to find the integer square root

        while left <= right:
            curr_sum = left * left + right * right

            if curr_sum == c:
                return True
            elif curr_sum < c:
                left += 1
            else:
                right -= 1

        return False