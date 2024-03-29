class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        area = -1
        while left < right:
            area = max(area, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return area
