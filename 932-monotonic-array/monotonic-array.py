class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc_flag = False
        dsc_flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dsc_flag = True
            elif nums[i] > nums[i - 1]:
                asc_flag = True
            else:
                pass

        return not (asc_flag and dsc_flag)
