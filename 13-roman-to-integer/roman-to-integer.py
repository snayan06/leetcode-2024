class Solution:
    def romanToInt(self, s: str) -> int:
        """
        basically we have to add and substract and remember prev_value
        """
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        prev_value = 0
        for char in reversed(s):
            value = roman_numerals[char]
            if value < prev_value:
                result = result - value
            else:
                result = result + value
            prev_value = value

        return result
