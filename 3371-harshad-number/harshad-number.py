class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        c = 0
        s1 = x
        while x > 0:
            rem = x % 10
            x = x // 10
            c += rem

        if s1 % c == 0:
            return c
        else:
            return -1