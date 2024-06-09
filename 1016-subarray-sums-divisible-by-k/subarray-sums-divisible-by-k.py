from typing import List


class Solution:
    """
    This solution finds the number of subarrays whose sum is divisible by k.

    Intuition:
    - We use a running sum to keep track of the cumulative sum of the elements.
    - We use a hashmap (mod_map) to store the indices of the prefix sums' remainders when divided by k.
    - If the same remainder is encountered again, it means that the subarray sum between these indices is divisible by k.
    - We handle the edge case of subarrays starting from the beginning by initializing the map with 0: [-1].

    Time Complexity:
    - O(n), where n is the length of the input array. We iterate through the array once.

    Space Complexity:
    - O(k), where k is the input integer. In the worst case, the map will store k different remainders.
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running = 0  # Running sum of elements
        count = 0  # Number of valid subarrays
        # Initialize mod_map with 0: [-1] to handle subarrays starting from index 0
        mod_map = {0: [-1]}

        result = []  # List to store all valid subarrays for debugging purposes

        for i, num in enumerate(nums):
            running += num  # Update the running sum
            rem = running % k  # Compute the remainder

            # Adjust for negative remainder to be positive
            if rem < 0:
                rem += k

            # If the remainder is already in mod_map, it means we found valid subarrays
            if rem in mod_map:
                # Increment the count by the number of times this remainder has been seen
                count += len(mod_map[rem])
                # for start_index in mod_map[rem]:
                #     # Append subarray from start_index + 1 to i
                #     result.append(nums[start_index + 1 : i + 1])
                mod_map[rem].append(i)
            else:
                mod_map[rem] = [
                    i
                ]  # Initialize with the current index if remainder is not in mod_map

            print(result)  # Print current list of valid subarrays for debugging

        return count
