class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Finds the numbers from 1 to n that are missing from the input array.

        Intuition:
        * The algorithm leverages the input array itself to mark the elements that are present.
        * The key is that numbers in the range [1, n] correspond to valid indices within the array.

        Approach:
        1. Iterate through the array:
            * For each element 'num', calculate the index it should map to: 'index = abs(num) - 1'. 
            * Mark the element at 'index' as negative to indicate the presence of the value 'abs(num)'.

        2. Iterate through the array again:
            * If an element 'nums[i]' is positive, it means the number 'i + 1' is missing. 
            * Append these missing numbers to the 'answer' list.

        Time Complexity:
        * O(n) since we have two loops iterating through the array of length n.

        Space Complexity:
        * O(1) as we modify the input array in-place.

        Args:
            nums: A list of integers, potentially with duplicates and missing values.

        Returns:
            A list of integers representing the missing numbers in the range [1, n].
        """

        answer = []
        n = len(nums)

        for i in range(n):
            nums[abs(nums[i]) - 1] = -1 * abs(nums[abs(nums[i]) - 1])

        for i in range(n):
            if nums[i] > 0:
                answer.append(i + 1)

        return answer 
