from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Find the number of subarrays in the given list of integers with exactly k distinct elements.

        Args:
        - nums (List[int]): A list of integers.
        - k (int): The desired number of distinct elements in the subarrays.

        Returns:
        - int: The number of subarrays with exactly k distinct elements.

        Intuition:
        - This solution calculates the count of subarrays with exactly k distinct elements by subtracting the count of subarrays
          with at most k-1 distinct elements from the count of subarrays with at most k distinct elements.

        Approach:
        - The function atMostK(nums, k) calculates the count of subarrays with at most k distinct elements using a sliding window approach.
        - It iterates through the list of integers using two pointers, left and right, to keep track of the current subarray.
        - A defaultdict is used to count the occurrences of each element in the current subarray.
        - The distinct variable keeps track of the number of distinct elements in the current subarray.
        - As the right pointer moves forward, elements are added to the counter and distinct is updated accordingly.
        - If the number of distinct elements exceeds k, the left pointer is moved forward until distinct becomes less than or equal to k.
        - The number of subarrays ending at the current right index with at most k distinct elements is calculated.
        - The result is updated with this count as the right pointer moves forward.
        - The function returns the difference between the counts of subarrays with at most k distinct elements and subarrays with at most k-1 distinct elements,
          which gives the count of subarrays with exactly k distinct elements.

        Complexity Analysis:
        - Time Complexity: O(n), where n is the length of the input array nums. Both the atMostK function and the main function iterate through the array once.
        - Space Complexity: O(n), where n is the length of the input array nums. The counter dictionary can store at most n distinct elements.
        """
        def atMostK(nums, k):
            counter = defaultdict(int)
            distinct = 0
            left = 0
            result = 0

            for right in range(len(nums)):
                if counter[nums[right]] == 0:
                    distinct += 1
                counter[nums[right]] += 1

                while distinct > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                result += right - left + 1

            return result

        return atMostK(nums, k) - atMostK(nums, k - 1)
