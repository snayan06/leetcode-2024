class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a given string is a palindrome after removing non-alphanumeric characters
        and ignoring case.

        Args:
        - s (str): Input string

        Returns:
        - bool: True if the string is a palindrome, False otherwise
        """

        # Create a cleaned-up string containing only alphanumeric characters
        cleaned_str = ""
        for char in s:
            char = char.lower()
            if char.isalnum():
                cleaned_str += char

        # Use two pointers approach to check if the cleaned string is a palindrome
        left = 0
        right = len(cleaned_str) - 1

        while left < right:
            if cleaned_str[left] != cleaned_str[right]:
                return False
            left += 1
            right -= 1

        return True