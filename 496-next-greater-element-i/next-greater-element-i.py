class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the next greater element for each element in nums1 in nums2.

        Intuition:
        - We can use a stack to find the next greater element efficiently.
        - Create a dictionary to store the index of each element in nums1 for easier lookup.
        - Initialize the result array with -1, which represents that there is no greater element found.
        - Iterate through nums2.
        - While the stack is not empty and the current element is greater than the top element of the stack:
            - Pop elements from the stack and update the result array with the current element if the popped element is in nums1.
        - Push the current element onto the stack.
        - Finally, return the result array.

        Time Complexity: O(N1 + N2)
        - N1 is the length of nums1 and N2 is the length of nums2.
        - We iterate through nums2 once, and for each element, we perform stack operations, which take O(1) time.

        Space Complexity: O(N1)
        - We use a stack and a dictionary to store indices of elements from nums1, which can take up to O(N1) space.
        """
        # Create index for easier lookup
        num1_index = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                if val in num1_index:
                    res[num1_index[val]] = num
            stack.append(num)

        return res
