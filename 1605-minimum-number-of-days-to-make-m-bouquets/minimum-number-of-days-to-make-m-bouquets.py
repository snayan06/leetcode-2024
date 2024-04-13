class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Find the minimum number of days to wait until you can make m bouquets, where each bouquet consists of k adjacent flowers blooming.

        Intuition:
        - We need to find the minimum number of days such that we can make m bouquets each containing k adjacent flowers.
        - We can use binary search to find the answer, searching for the minimum possible day where it's possible to make m bouquets.
        - The possible function determines if it's possible to make m bouquets within a given number of days.
        - We start with the smallest and largest possible days and adjust the search space using binary search.

        Time Complexity: O(n * log(max(bloomDay)))
        - Binary search is performed on the range of bloomDay, which takes O(log(max(bloomDay))) time.
        - The `possible` function iterates through the bloomDay array once, which takes O(n) time.

        Space Complexity: O(1)
        - The algorithm uses only a constant amount of extra space for variables, regardless of the input size.

        Args:
        - bloomDay: A list of integers representing the blooming day of each flower.
        - m: The number of bouquets to make.
        - k: The number of adjacent flowers needed to make a bouquet.

        Returns:
        - The minimum number of days required to make m bouquets, or -1 if it's impossible.
        """
        if m * k > len(bloomDay):
            return -1

        def possible(day):
            cnt = 0  # Count of flowers bloomed in current interval
            no_of_b = 0  # Number of bouquets made
            for bloom in bloomDay:
                if bloom <= day:
                    cnt += 1
                else:
                    no_of_b += (
                        cnt // k
                    )  # Calculate number of bouquets possible with flowers bloomed so far
                    cnt = 0  # Reset count for the next interval
            no_of_b += cnt // k  # Calculate number of bouquets with remaining flowers
            return no_of_b >= m  # Check if the required number of bouquets can be made

        low = min(bloomDay)  # Minimum possible day
        high = max(bloomDay)  # Maximum possible day

        while low <= high:
            mid = low + (high - low) // 2  # Calculate mid day
            if possible(mid):  # If it's possible to make m bouquets with mid day
                high = mid - 1  # Update high to search for smaller days
            else:
                low = mid + 1  # Update low to search for larger days
        return low  # Return the minimum number of days required
