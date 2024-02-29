from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if there are any duplicate elements in the given list.

        Intuition:
        The function uses a hash set to keep track of unique elements encountered
        while iterating through the list. If an element is already in the hash set,
        it means there is a duplicate, and the function returns True. Otherwise, the
        element is added to the hash set. If the entire list is iterated without
        finding any duplicates, the function returns False.

        Time Complexity:
        The time complexity is O(n), where n is the length of the input list. This is
        because, in the worst case, the function may need to iterate through the entire
        list to determine if there are any duplicates.

        Space Complexity:
        The space complexity is O(n), where n is the length of the input list. In the
        worst case, the hash set may store all unique elements of the list.
        """
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        
        return False
