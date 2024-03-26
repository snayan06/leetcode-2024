class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 1. Handle out-of-range elements efficiently
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # 2. Use the input array itself for presence marking
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                # Avoid redundant marking if already negative
                if nums[val - 1] > 0: 
                    nums[val - 1] = -nums[val - 1] 

        # 3. Find the missing positive integer
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # 4. All positive integers within range were present 
        return n + 1
