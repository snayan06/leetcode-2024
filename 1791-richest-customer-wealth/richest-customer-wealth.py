from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Find the maximum wealth among the given accounts.

        Args:
        - accounts (List[List[int]]): A list of accounts where each account is represented
                                      as a list of integers indicating wealth.

        Returns:
        - int: The maximum wealth among all the accounts.

        Intuition:
        - Iterate through each account and calculate the sum of wealth.
        - Keep track of the maximum wealth encountered during the iteration.

        Time Complexity:
        - O(m * n), where m is the number of accounts and n is the average number of elements
          in each account. The algorithm iterates through each account and calculates the sum.

        Space Complexity:
        - O(1), constant space is used to store the maximum wealth.
        """
        max_wealth = 0

        # Iterate through each account
        for account in accounts:
            # Calculate the sum of wealth for the current account
            current_wealth = sum(account)

            # Update the maximum wealth if the current account's wealth is greater
            max_wealth = max(max_wealth, current_wealth)

        return max_wealth
