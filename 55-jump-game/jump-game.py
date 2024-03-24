class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_good_index = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= last_good_index:
                last_good_index = i
            print(last_good_index)
            if last_good_index == 0:
                return 1

        return 0
