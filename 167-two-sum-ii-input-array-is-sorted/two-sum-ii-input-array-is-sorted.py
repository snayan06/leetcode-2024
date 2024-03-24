class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in the sorted array 'numbers' that add up to 'target'.

        Args:
        - numbers (List[int]): A sorted list of integers.
        - target (int): The target sum.

        Returns:
        - List[int]: A list containing the indices (1-indexed) of the two numbers that add up to the target sum.

        Intuition:
        The problem can be solved using two different approaches:

        Approach 1: Hash Table
        - Maintain a hash table to store the index of each number as we traverse the array.
        - For each number, calculate the complement (target - current number) and check if it exists in the hash table.
        - If found, return the indices of the current number and its complement.
        - This approach has a time complexity of O(n) and a space complexity of O(n).

        Approach 2: Two Pointer
        - Use two pointers, 'left' and 'right', initialized at the beginning and end of the array, respectively.
        - Since the array is sorted, if the sum of the numbers at 'left' and 'right' pointers is equal to the target,
          return the indices of these numbers.
        - If the sum is greater than the target, decrement 'right' to consider a smaller number.
        - If the sum is less than the target, increment 'left' to consider a larger number.
        - This approach has a time complexity of O(n) and a space complexity of O(1).

        """
        # Approach 1: Hash Table
        # index_dict = {}
        # for index, num in enumerate(numbers):
        #     seek_value = target - num
        #     if seek_value in index_dict:
        #         return [index_dict[seek_value]+1, index+1]
        #     index_dict[num] = index

        # Approach 2: Two Pointer
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]  # Indices are 1-indexed
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return []  # If no such pair is found, return an empty list
