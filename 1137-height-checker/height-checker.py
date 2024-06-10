class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        array = heights.copy()
        array.sort()
        count = 0
        for i, height in enumerate(heights):
            if array[i] != height:
                count += 1

        return count
