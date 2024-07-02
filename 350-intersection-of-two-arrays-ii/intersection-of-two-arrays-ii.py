class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2 = {}

        for num in nums1:
            if not d1.get(num):
                d1[num] = 1
            else:
                d1[num] += 1

        for num in nums2:
            if not d2.get(num):
                d2[num] = 1
            else:
                d2[num] += 1

        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set1.intersection(set2)
        answer = []
        for num in list(set3):
            len1 = d1.get(num)
            len2 = d2.get(num)
            r = min(len1, len2)

            for i in range(r):
                answer.append(num)

        return answer
