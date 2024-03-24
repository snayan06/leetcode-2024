class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_dict = {}
        for index, num in enumerate(numbers):
            seek_value = target - num
            if seek_value in index_dict:
                return [index_dict[seek_value]+1, index+1]
            index_dict[num] = index