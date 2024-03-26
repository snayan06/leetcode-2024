class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Finds duplicate numbers in an input array.

        Intuition:
        * The core idea is to use the input array itself as a 'presence map'.
        * Each element's value (within the range [1, n]) can be mapped to a corresponding index.
        * By making the element at that index negative, we mark the presence of that number.
        * If we encounter a negative element later, it signifies a duplicate.

        Approach:
        1. Iterate through the array.
        2. For each element 'num', calculate its corresponding 'index' (abs(num) - 1).
        3. If 'nums[index]' is already negative, 'abs(num)' is a duplicate; add it to 'answer'.
        4. Mark 'nums[index]' as negative.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            nums: A list of integers containing duplicates.

        Returns:
            A list of the duplicate integers found in the input array.
        """

        answer = []
        n = len(nums)

        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                answer.append(index + 1)
            nums[index] = -nums[index]

        return answer
