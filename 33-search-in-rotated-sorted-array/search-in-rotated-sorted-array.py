class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search on a rotated sorted array to find the index of a target element.

        Intuition:
        - The given array is rotated, meaning it may not be sorted in ascending order, but it's still partially sorted.
        - We utilize binary search because it efficiently narrows down the search space.
        - At each step, we identify which half of the array is sorted and check if the target lies within that sorted half.
        - If the target is within the sorted half, we adjust the search boundaries accordingly.
        - If the target is not within the sorted half, we discard that half and search the other half.
        - This approach allows us to find the target element efficiently in O(log n) time complexity.

        Time Complexity: O(log n)
        - The binary search algorithm halves the search space in each iteration, leading to logarithmic time complexity.

        Space Complexity: O(1)
        - The algorithm uses only a constant amount of extra space for variables, regardless of the input size.

        Args:
        - nums: A list of integers representing the rotated sorted array.
        - target: The integer value we are searching for within the array.

        Returns:
        - If the target is found, return its index. If not found, return -1.
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
