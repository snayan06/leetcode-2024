class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters in a given string.

        Args:
        - s (str): Input string

        Returns:
        - int: Length of the longest substring without repeating characters

        Intuition:
        - This solution uses the sliding window approach with two pointers: `l` and `r`.
        - The dictionary `d` is used to map characters to their latest index of occurrence.
        - We start with `l` and `r` both at the beginning of the string.
        - As we iterate through the string, we update `r` and check if the character at index `r` is already in the dictionary `d`.
        - If it is, we update `l` to the maximum of its current value and the index of the repeated character plus one.
        - We update the `answer` with the maximum of its current value and the length of the current substring (`r - l + 1`).
        - Finally, we update the dictionary `d` with the index of the current character and move `r` to the next position.
        - The process continues until `r` reaches the end of the string.
        - The maximum length of a substring without repeating characters is stored in `answer`.

        Time Complexity:
        - O(n), where n is the length of the input string `s`.
          The algorithm iterates through the string once.

        Space Complexity:
        - O(min(n, m)), where n is the length of the input string `s` and m is the size of the character set (ASCII characters).
          The space used by the dictionary `d` is bounded by the size of the character set.
        """
        l = 0
        r = 0
        d = {}
        answer = -1

        while r < len(s):
            if s[r] in d:
                l = max(l, d[s[r]] + 1)

            answer = max(answer, r - l + 1)
            d[s[r]] = r
            r += 1

        return max(answer, r - l)
