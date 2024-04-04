class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create index for easier lookup
        num1_index = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                if val in num1_index:
                    res[num1_index[val]] = num
            stack.append(num)

        return res
