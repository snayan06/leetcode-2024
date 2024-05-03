class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = list(map(int, version1.split(".")))
        l2 = list(map(int, version2.split(".")))

        # Adjust the lengths of version lists by appending zeros if necessary
        len_diff = len(l1) - len(l2)
        if len_diff < 0:
            l1.extend([0] * abs(len_diff))
        elif len_diff > 0:
            l2.extend([0] * len_diff)

        # Compare versions
        for v1, v2 in zip(l1, l2):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0  # Versions are equal
