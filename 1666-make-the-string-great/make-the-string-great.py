class Solution:
    def makeGood(self, s: str) -> str:
        """
        Removes adjacent characters in the string 's' that form pairs of one uppercase
        and one lowercase letter of the same type. Returns the modified string.

        Time Complexity: O(n)
        - The algorithm iterates through each character of the string once.

        Space Complexity: O(n)
        - In the worst case, the stack may contain all characters of the string.

        Intuition:
        1. We utilize a stack to efficiently remove adjacent characters forming invalid pairs.
        2. As we iterate through the string, we compare the current character with the top of the stack.
        3. If they form an invalid pair (one uppercase and one lowercase of the same letter), we pop the stack.
        4. Otherwise, we push the current character onto the stack.
        5. The resulting stack will contain characters that do not form invalid pairs, thus giving us the desired result.
        """
        stack = []  # Initialize an empty stack to track characters
        invalid_condn = [32, -32]  # Conditions for characters forming invalid pairs

        for char in s:
            if stack and (ord(stack[-1]) - ord(char) in invalid_condn):
                stack.pop()  # Remove the previous character if it forms an invalid pair with the current character
            else:
                stack.append(char)  # Push the current character onto the stack

        return "".join(stack)  # Convert the stack to a string and return it
