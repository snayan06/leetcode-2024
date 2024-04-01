from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with at most k replacements.

        Intuition:
        - We use a sliding window approach where we maintain a window [l, r] that represents the current substring.
        - We keep track of the frequency of characters within the window using a counter dictionary.
        - The variable 'mf' keeps track of the most frequent character count in the current window.
        - We iterate over the string using the right pointer 'r', and update the character count in the counter dictionary.
        - Whenever we encounter a character, we update 'mf' to be the maximum frequency of any character in the current window.
        - To ensure that we maintain at most k replacements, we keep shrinking the window from the left side 'l' whenever the length of the window minus 'mf' exceeds 'k'.
        - Finally, we update the answer with the maximum length of a valid substring found so far.

        Time Complexity: O(n)
        - The algorithm traverses the string once from left to right.

        Space Complexity: O(1)
        - The space used by the counter dictionary is bounded by the number of unique characters in the alphabet, which is constant.
        """
        l, r = 0, 0
        most_frequent = 0
        counter = defaultdict(int)
        answer = 0

        while r < len(s):
            counter[s[r]] += 1
            most_frequent = max(most_frequent, counter[s[r]])

            if (r - l + 1 - most_frequent) > k:
                if counter[s[l]] == 1:
                    del counter[s[l]]
                else:
                    counter[s[l]] -= 1
                most_frequent = max(counter.values()) if counter else 0
                l += 1 
            
            if (r - l + 1 - most_frequent) <= k:
                answer = max(answer, r - l + 1)

            r += 1

        return answer
