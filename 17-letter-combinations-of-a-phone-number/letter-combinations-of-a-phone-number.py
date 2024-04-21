class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations represented by a digit string using 
        a recursive approach.

        Intuition:
        Imagine a decision tree where each level represents a digit, and branches 
        correspond to the letters mapped to that digit. The recursive function explores 
        all possible paths through this tree, building combinations letter by letter.

        Recursive Process:
        1. Base Case: If we've built a combination the same length as the input digits, 
           add it to the result.
        2. Recursive Step: For the current digit, try each of its corresponding letters:
            * Add the letter to the growing combination.
            * Recursively explore possibilities for the next digit.
            * Remove the letter (backtracking) to try other combinations.
       """

        answer = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []  # Handle the case of an empty digit string

        def helperFunc(answer, combination, pointer):
            if pointer == len(digits):
                answer.append(combination)
                return

            digit = digits[pointer]
            letters = mapping[digit]

            for letter in letters:
                helperFunc(answer, combination + letter, pointer + 1)

        helperFunc(answer, "", 0)
        return answer
