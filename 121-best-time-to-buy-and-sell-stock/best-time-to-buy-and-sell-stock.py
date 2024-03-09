from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit that can be obtained from buying and selling stocks.

        Args:
        - prices (List[int]): A list of stock prices for each day.

        Returns:
        - int: The maximum profit that can be obtained.

        Intuition:
        - The approach is to iterate through the prices and keep track of the minimum stock price.
          Calculate the potential profit at each step by subtracting the minimum stock price from the current price.
          Update the maximum profit if the calculated profit is greater.

        Time Complexity:
        - O(n), where n is the number of days (length of the prices list).
          The algorithm iterates through the list once.

        Space Complexity:
        - O(1), constant space is used for variables (max_profit, min_stock_price).
        """
        max_profit = 0
        min_stock_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_stock_price and i!=len(prices)-1:
                min_stock_price = prices[i]
            else:
                max_profit = max(prices[i] - min_stock_price, max_profit)
        
        return max_profit
