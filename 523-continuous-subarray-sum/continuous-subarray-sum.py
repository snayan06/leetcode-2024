class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        mod_map = {0: -1}
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            mod = current_sum % k
            if mod < 0:
                mod += k

            if mod in mod_map:
                if i - mod_map[mod] > 1:
                    return True
            else:
                # Store the index of the first occurrence of this mod
                mod_map[mod] = i
