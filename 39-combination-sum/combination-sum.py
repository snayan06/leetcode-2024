class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = []
        n = len(candidates)

        def helperFunc(index, target, ds):
            # base case
            if index == n:
                if target == 0:
                    answer.append(list(ds))
                return

            # choose
            if target - candidates[index] >= 0:
                ds.append(candidates[index])
                helperFunc(index, target - candidates[index], ds)
                # backtrack
                ds.pop()
            # unchoose
            helperFunc(index + 1, target, ds)

        helperFunc(0, target, [])

        return answer
