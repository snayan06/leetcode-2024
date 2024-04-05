from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Finds the number of days you would have to wait until a warmer temperature by comparing each day's temperature with the temperatures of subsequent days.

        Intuition:
        - We use a stack to keep track of the indices of temperatures.
        - Iterate through each day's temperature:
            - While the stack is not empty and the temperature of the current day is warmer than the temperature of the day at the top of the stack:
                - Pop the index of the colder day from the stack and calculate the number of days until a warmer temperature (current day's index - index of colder day).
                - Update the result array at the index of the colder day with the number of days.
            - Push the index of the current day onto the stack.
        - Return the result array containing the number of days to wait for a warmer temperature for each day.

        This problem is similar to the "Next Greater Element" question, where we need to find the next greater element for each element in an array, but with a slight variation.

        Time Complexity: O(N)
        - We iterate through the temperatures array once.

        Space Complexity: O(N)
        - We use a stack to store indices, which can take up to O(N) space.
        - The result array also takes O(N) space.
        """
        stack = []
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            tmp = temperatures[i]
            while stack and temperatures[stack[-1]] < tmp:
                val = stack.pop()
                result[val] = i - val
            stack.append(i)

        return result
