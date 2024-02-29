class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):

            count[nums[i]] = count.get(nums[i], 0) + 1

        flag = False
        for v in sorted(count.values(), reverse=True):
            if v > 1:
                flag = True
                break

        return flag
