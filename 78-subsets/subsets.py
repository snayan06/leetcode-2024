class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        n = len(nums)

        def helperFunc(ds, index):
            # base-case
            if index >= n:
                all_subsets.append(list(ds))
                return

            # choose
            ds.append(nums[index])
            helperFunc(ds, index + 1)
            # unchoose
            ds.pop()
            helperFunc(ds, index + 1)

        helperFunc([], 0)
        return all_subsets
