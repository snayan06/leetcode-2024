class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string 's' consisting of words separated by spaces, 
        returns the length of the last word. If there is no last word, 
        or if the string is empty after stripping leading and trailing 
        whitespaces, returns 0.

        Parameters:
        - s (str): Input string containing words.

        Returns:
        - int: Length of the last word in the string.

        Solution Logic:
        - Strip leading and trailing whitespaces from the input string.
        - Split the string into a list of words using space as the delimiter.
        - Return the length of the last word in the list.
        """
        ss = s.strip()
        s = ss.split(" ")
        return len(s[-1])
        