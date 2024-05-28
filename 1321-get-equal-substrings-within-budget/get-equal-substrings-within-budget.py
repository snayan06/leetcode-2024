class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # lets first take the cost and sort it
        cost = []
        for i in range(len(s)):
            cost.append(abs(ord(s[i]) - ord(t[i])))

        left = 0
        right = 0

        total_cost = 0
        max_length = 0

        for right in range(len(cost)):

            total_cost += cost[right]

            while total_cost > maxCost:
                total_cost -= cost[left]
                left += 1

            window_size = right - left + 1
            max_length = max(max_length, window_size)

        return max_length
