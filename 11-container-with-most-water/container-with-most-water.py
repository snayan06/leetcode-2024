class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ma = float("-inf")
        while left < right:
            ma = max(min(height[left], height[right]) * abs(left - right), ma)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ma
