class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            tmp = temperatures[i]
            while stack and temperatures[stack[-1]] < tmp:
                val = stack.pop()
                result[val] = i - val
            stack.append(i)

        return result
