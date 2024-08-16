from typing import List

class Solution:
    """
    This solution finds the number of subarrays whose sum is divisible by k.

    Intuition:
    - We use a running sum to keep track of the cumulative sum of the elements.
    - We use a hashmap (prefix_sum) to store the count of remainders when the cumulative sum is divided by k.
    - If the same remainder is encountered again, it means that the subarray sum between these indices is divisible by k.

    Time Complexity:
    - O(n), where n is the length of the input array. We iterate through the array once.

    Space Complexity:
    - O(k), where k is the input integer. In the worst case, the map will store k different remainders.
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}  # Initialize with remainder 0 seen once
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            rem = curr_sum % k
            
            # Directly check if remainder is present in the map
            if rem in prefix_sum:
                count += prefix_sum[rem]
            
            # Update the remainder count in the dictionary
            prefix_sum[rem] = prefix_sum.get(rem, 0) + 1

        return count
