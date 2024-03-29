from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array which gives the sum of zero.

        Intuition:
        The problem requires finding unique triplets in an array such that their sum equals zero.
        One approach is to sort the array and then iterate through it. For each element nums[i],
        use a two-pointer technique to find two other elements that sum up to the target (zero).

        Approach:
        1. Sort the input array nums.
        2. Iterate through the array using a loop.
        3. For each element nums[i], use two pointers - one starting from i+1 and another from the end of the array.
        4. Move the pointers towards each other and check the sum.
        5. If the sum is zero, append the triplet to the answer list and move the pointers accordingly.
        6. If the sum is greater than zero, decrement the right pointer.
        7. If the sum is less than zero, increment the left pointer.
        8. Skip duplicates to avoid duplicate triplets.

        Time Complexity:
        Sorting the array takes O(n log n) time. The main loop runs in O(n) time. Within the loop,
        the two-pointer technique also takes O(n) time. Thus, the overall time complexity is O(n^2).

        Space Complexity:
        The space complexity is O(1) as we are using only a constant amount of extra space.

        Args:
        nums (List[int]): Input array of integers.

        Returns:
        List[List[int]]: List of unique triplets whose sum is zero.
        """
        answer = []
        nums.sort()
        n = len(nums)
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1
        return answer
