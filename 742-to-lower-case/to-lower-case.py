class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Given a string 's', returns the string after replacing every 
        uppercase letter with the corresponding lowercase letter using ASCII values.

        Parameters:
        - s (str): Input string.

        Returns:
        - str: String with all uppercase letters converted to lowercase.

        Solution Logic:
        - Iterate through each character in the string.
        - Check if the character is an uppercase letter using ASCII values.
        - If it is, convert it to lowercase using ASCII values.
        - Build the result string character by character.
        """
        result = ""
        for char in s:
            # Check if the character is an uppercase letter
            if 'A' <= char <= 'Z':
                # Convert to lowercase using ASCII values
                result += chr(ord(char) + 32)
            else:
                result += char
        return result