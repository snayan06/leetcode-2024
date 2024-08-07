class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = global_max = nums[0]
        n = len(nums)
        for i in range(1,n):
            local_max = max(nums[i] ,nums[i]+ local_max)

            global_max = max(global_max, local_max)
        
        return global_max
        