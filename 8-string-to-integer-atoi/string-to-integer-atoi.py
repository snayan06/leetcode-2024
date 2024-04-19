class Solution:
    def myAtoi(self, s: str) -> int:
        def func(s, i, n, digitsStarted, ans):
            if i>=n:
                return ans
            if digitsStarted:    
                if s[i] in '1234567890':
                    ans = ans*10 + int(s[i])
                    return func(s, i+1,n, True, ans)
                else:
                    return ans
            if s[i] == ' ':
                return func(s, i+1,n, False, ans)
                
            if s[i] == '-':
                return -1 * func(s, i+1,n, True, ans)

            if s[i] == '+':
                return func(s, i+1,n, True, ans)
                        
            if s[i] in '1234567890':
                return func(s, i+1, n, True, int(s[i]))
            return 0

        ans = func(s, 0, len(s), False, 0)
        if ans < -2**31:
            return -2**31
        elif ans> 2**31 - 1:
            return 2**31 - 1
        else:
            return ans
        




        