from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find the indices of two numbers in the given list that add up to the target.

        Intuition:
        The function uses a dictionary to store the indices of numbers as it iterates through
        the list. For each number, it calculates the difference (seek_value) between the target
        and the current number. If the seek_value is already in the dictionary, it means that
        the current number, along with the number at the seek_value index, adds up to the target.

        Time Complexity:
        The time complexity is O(n), where n is the length of the input list. The function
        iterates through the list once, and dictionary operations take constant time on average.

        Space Complexity:
        The space complexity is O(n), where n is the length of the input list. The dictionary
        stores the indices of numbers encountered during the iteration.
        """
        index_dict = {}
        for index, num in enumerate(nums):
            seek_value = target - num
            if seek_value in index_dict:
                return [index_dict[seek_value], index]
            index_dict[num] = index
