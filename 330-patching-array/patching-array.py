class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        Given a sorted integer array nums and an integer n, this function determines 
        the minimum number of patches required to ensure that any number in the range 
        [1, n] can be formed by the sum of some elements in the array.

        Intuition:
        The key to solving this problem is to always focus on the smallest number (`miss`) 
        that we cannot currently form using the elements of the array and any patches 
        we've added. By ensuring we can form the smallest missing number, we can extend 
        our range of formable numbers efficiently.

        Steps:
        1. Initialize `miss` to 1, which is the smallest number we need to form initially.
        2. Initialize `patches` to 0 to count the number of patches added.
        3. Use an index `i` to iterate through the `nums` array.
        4. While `miss` is less than or equal to `n`:
           - If the current element in `nums` (i.e., `nums[i]`) is less than or equal to `miss`, 
             use it to extend the range of formable numbers, and move to the next element.
           - If `nums[i]` is greater than `miss` or we have exhausted the array, patch the 
             array by adding `miss` itself. This effectively doubles the range of numbers 
             we can form.
        5. Repeat until `miss` exceeds `n`.
        6. Return the number of patches required.

        This greedy approach ensures that we always address the smallest missing number, 
        thereby covering the entire range [1, n] with the minimum number of patches.
        
        Args:
        nums (List[int]): A sorted list of integers.
        n (int): The upper limit of the range [1, n].

        Returns:
        int: The minimum number of patches required.
        """
        
        miss = 1
        patches = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        
        return patches
