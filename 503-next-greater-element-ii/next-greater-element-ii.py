from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Finds the next greater element for each element in the given array.

        Intuition:
        - We can use a stack to find the next greater element efficiently.
        - Since we might need to traverse the array again to find the next greater element for elements towards the end of the array, 
          we'll concatenate the array with itself to handle such cases.
        - Initialize the result array with -1, which represents that there is no greater element found.
        - Iterate through the doubled nums array.
        - While the stack is not empty and the current element is greater than the top element of the stack:
            - Pop elements from the stack and update the result array with the current element.
        - Push the current element onto the stack.
        - Finally, return the result array.

        Time Complexity: O(N)
        - We iterate through the doubled nums array once.

        Space Complexity: O(N)
        - We use a stack to store elements, which can take up to O(N) space.
        """
        n = len(nums)
        nums = nums + nums
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[i] > nums[stack[-1]]:
                val = stack.pop()
                result[val % n] = nums[i]

            stack.append(i)

        return result
