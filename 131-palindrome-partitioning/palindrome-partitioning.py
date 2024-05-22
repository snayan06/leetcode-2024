class Solution:
    def is_palindrome(self,s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def helperFunc(s, index, ds):

            if index == len(s):
                answer.append(list(ds))
                return

            for i in range(index, len(s)):
                substr = s[index : i + 1]

                if self.is_palindrome(substr):
                    ds.append(substr)
                    helperFunc(s, i + 1, ds)
                    ds.pop()

        helperFunc(s, 0, [])

        return answer
