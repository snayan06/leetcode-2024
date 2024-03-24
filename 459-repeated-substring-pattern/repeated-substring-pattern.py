class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Check if the given string is a repeated substring pattern.

        Args:
        - s (str): The input string to be checked.

        Returns:
        - bool: True if the string is a repeated substring pattern, False otherwise.

        Intuition:
        - One approach is to consider every substring of the input string that is less than
          half its length. Check if the string can be formed by repeating this substring.
          If such a substring is found, return True.
        - Another approach is to concatenate the input string with itself (s + s), then
          remove the first and last characters. If the original string is found within this
          concatenated string, it means the original string can be formed by repeating a
          substring, and thus return True.

        Time Complexity:
        - Approach 1: O(n^2), where n is the length of the input string.
          This approach involves iterating through substrings of the input string.
        - Approach 2: O(n), where n is the length of the input string.
          This approach involves concatenating the string with itself and performing a search.

        Space Complexity:
        - Approach 1: O(n), where n is the length of the input string.
          This is the space required to store the substring.
        - Approach 2: O(n), where n is the length of the input string.
          This is the space required to store the concatenated string.
        """
        # Approach 2: Check if the string can be formed by repeating a substring
        result = (s + s).find(s, 1) < len(s)
        return result
