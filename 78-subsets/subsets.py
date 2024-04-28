from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of the given list of integers.

        Approach / Intuition:
        We can solve this problem using backtracking. The idea is to start with an empty subset and then recursively explore all possible subsets by either including or excluding each element of the input list. Imagine building all possible subsets as constructing a binary tree. At each step, we have two choices: include the current element in the subset or exclude it. By recursively exploring both choices, we can generate all subsets of the input list.

        Detailed Steps:
        1. Start with an empty subset.
        2. For each element in the input list:
            - Include the current element in the subset and move to the next element.
            - Exclude the current element from the subset and move to the next element.
        3. When we reach the end of the input list, append the current subset to the answer list.
        4. During backtracking, remove the last element from the current subset to explore different combinations.

        Time Complexity:
        The time complexity is O(2^N), where N is the number of elements in the input list. This is because for each element, we have two choices (include or exclude), and there are a total of 2^N possible subsets.

        Space Complexity:
        The space complexity is O(N * 2^N), where N is the number of elements in the input list. This is because we generate a total of 2^N subsets, each containing an average of N/2 elements.
        """
        answer = []
        n = len(nums)

        def helperFunc(index, ds):
            if index >= n:
                answer.append(list(ds))
                return 
            
            # choose 
            ds.append(nums[index])
            helperFunc(index + 1, ds)
            # backtrack
            ds.pop()
            # unchoose
            helperFunc(index + 1, ds)
        
        helperFunc(0, [])

        return answer
