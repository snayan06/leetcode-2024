class Solution:
    def maxDepth(self, s: str) -> int:

        max_counter = 0
        counter = 0
        for char in s:
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1
            max_counter = max(counter, max_counter)

        return max_counter
