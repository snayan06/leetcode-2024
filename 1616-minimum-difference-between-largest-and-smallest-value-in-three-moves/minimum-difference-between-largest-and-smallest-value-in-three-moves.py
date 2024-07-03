class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
    
    # We can consider changing 0, 1, 2, or 3 smallest or largest elements
        return min(
        nums[-1] - nums[3],  # Change 3 smallest
        nums[-2] - nums[2],  # Change 2 smallest and 1 largest
        nums[-3] - nums[1],  # Change 1 smallest and 2 largest
        nums[-4] - nums[0]   # Change 3 largest
    )
        