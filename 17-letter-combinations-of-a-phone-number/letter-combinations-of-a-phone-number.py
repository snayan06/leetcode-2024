class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
            return []
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
