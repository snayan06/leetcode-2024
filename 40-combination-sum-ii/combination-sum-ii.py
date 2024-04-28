class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates that sum up to the target value.

        Intuition:
        - This problem can be solved using backtracking, where we recursively explore all possible combinations of candidates.
        - We sort the candidates array to handle duplicates and ensure that candidates are in ascending order.
        - At each step, we have two choices: include the current candidate or skip it.
        - To avoid generating duplicate combinations, we skip over duplicate candidates when exploring.
        - If the sum of the current combination equals the target, we add it to the answer list.
        - After exploring each candidate, we backtrack by removing the last candidate to explore other possibilities.

        Time Complexity:
        - Let N be the number of candidates and T be the target value.
        - Sorting the candidates array takes O(N log N) time.
        - The time complexity of the backtracking algorithm is O(2^N), where N is the number of candidates.
        - At each step, we have two choices (include or skip) for each candidate, resulting in exponential time complexity.
        - Therefore, the overall time complexity is O(N log N + 2^N).

        Space Complexity:
        - The space complexity is O(T) for the recursive call stack, where T is the target value.
        - Additionally, the space complexity of the output list is O(2^N * T) in the worst case.
        - Hence, the overall space complexity is O(2^N * T).

        :param candidates: List of candidate integers.
        :param target: Target integer.
        :return: List of lists containing unique combinations of candidates that sum up to the target value.
        """
        answer = []
        n = len(candidates)

        # Sort the candidates array to handle duplicates and ensure ascending order
        candidates.sort()

        def helperFunc(index, target, ds):
            # Base case: If target is 0, add the current combination to the answer list
            if target == 0:
                answer.append(list(ds))
                return

            # Explore candidates starting from the current index
            for i in range(index, n):
                # Skip duplicates and avoid generating duplicate combinations
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # If the current candidate exceeds the target, break the loop
                if target - candidates[i] < 0:
                    break

                # Choose the current candidate and recursively explore
                ds.append(candidates[i])
                helperFunc(i + 1, target - candidates[i], ds)

                # Backtrack: Remove the last candidate to explore other possibilities
                ds.pop()

        # Start the recursive exploration from the beginning of the candidates list
        helperFunc(0, target, [])

        return answer
