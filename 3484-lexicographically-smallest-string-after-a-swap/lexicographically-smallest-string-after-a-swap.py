class Solution:
    def getSmallestString(self, s: str) -> str:
        s_list = list(s)
        n = len(s_list)
        
        for i in range(n - 1):
            if (int(s_list[i]) % 2 == int(s_list[i + 1]) % 2):  # Check for "oo" or "ee"
                if s_list[i] > s_list[i + 1]:
                    s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
                    break

        return "".join(s_list)