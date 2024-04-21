class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        s = ""

        def helperFunc(answer, s, left, right):
            # base case

            if left == 0 and right == 0:
                answer.append(s)

            if left > 0:
                helperFunc(answer, s + "(", left - 1, right)
            if left < right and right > 0:
                helperFunc(answer, s + ")", left, right - 1)
        
        helperFunc(answer, "", n, n)

        return answer