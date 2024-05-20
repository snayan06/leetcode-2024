class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(start, path):
            all_subsets.append(list(path))

            for i in range(start, len(nums)):
                # Choose
                path.append(nums[i])
                # Recurse: Move on to the next element
                backtrack(i + 1, path)
                # unchoose
                path.pop()

        all_subsets = []
        backtrack(0, [])
        print(all_subsets)
        total_xor_sum = 0
        for subset in all_subsets:
            subset_xor = 0
            for num in subset:
                subset_xor ^= num  # XOR all elements in the subset
            total_xor_sum += subset_xor

        return total_xor_sum
