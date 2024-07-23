class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        d = sorted(d.items(),key=lambda item:(item[1],-item[0]))
        answer = []
        for key,value in d:
            while value > 0:
                answer.append(key)
                value -= 1
        return answer
