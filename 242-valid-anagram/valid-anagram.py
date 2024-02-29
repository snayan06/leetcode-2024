from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams.

        Intuition:
        The function uses a defaultdict to count the occurrences of each character in string 's'.
        Then, it subtracts the occurrences of each character in string 't'. If the strings are
        anagrams, the count for each character should be zero after this process.

        Time Complexity:
        The time complexity is O(max(len(s), len(t))). The function iterates through both strings,
        and the defaultdict operations take constant time per character.

        Space Complexity:
        The space complexity is O(unique_characters). The defaultdict stores the count for unique
        characters in string 's'.
        """
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        for c in t:
            count[c] -= 1

        for value in count.values():
            if value != 0:
                return False

        return True
