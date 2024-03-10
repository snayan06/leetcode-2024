from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate the product of elements except self for each element in the input array.

        Args:
        - nums (List[int]): Input array of integers.

        Returns:
        - List[int]: An array where each element is the product of all elements in the input array except itself.

        Intuition:
        - Two approaches are provided for solving the problem.

        Approach 1:
        - Use prefix and postfix arrays to store products to the left and right of each element.
        - Multiply corresponding prefix and postfix values for each element to get the final result.

        Approach 2:
        - Achieve the same result in a single array by first calculating products to the left of each element
          and then combining them with products to the right.

        Time Complexity:
        - O(n), where n is the length of the input array.
          Both approaches make two passes over the array, each taking linear time.

        Space Complexity:
        - Approach 1: O(n), additional space is used for prefix and postfix arrays.
        - Approach 2: O(1), no additional space is used apart from the output array.
        """
        n = len(nums)
        # Approach 1:
        # pre_pro = [1] * n
        # pre_pro[0] = 1
        # for i in range(1, n):
        #     pre_pro[i] = pre_pro[i - 1] * nums[i - 1]
        # post_pro = [0] * n
        # post_pro[n - 1] = 1
        # for i in range(n - 2, -1, -1):
        #     post_pro[i] = post_pro[i + 1] * nums[i + 1]
        # result = [pre_pro[i] * post_pro[i] for i in range(0, n)]

        # Approach 2:
        result = [1] * n
        temp = 1

        # Calculate products to the left and store in the result array
        for i in range(n):
            result[i] *= temp
            temp *= nums[i]

        temp = 1

        # Calculate products to the right and combine with the left products
        for i in range(n - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]

        return result