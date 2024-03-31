class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float('inf')
        n = len(nums)
        
        for i in range(n):
            for j in range(i, n):
                subarray = nums[i:j+1]
                bitwise_or_result = 0
                
                for num in subarray:
                    bitwise_or_result |= num
                    
                # Check if the condition is met
                if bitwise_or_result >= k:
                    min_length = min(min_length, len(subarray))
        
        return min_length if min_length != float('inf') else -1