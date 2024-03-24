class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        result = (s + s).find(s, 1) < len(s)
        return result
        