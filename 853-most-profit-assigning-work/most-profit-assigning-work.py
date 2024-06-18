class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # Step 1: Pair difficulties with profits and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Step 2: Sort worker abilities
        worker.sort()

        max_profit = (
            0  # To keep track of the maximum profit so far for any difficulty level
        )
        total_profit = 0  # To accumulate the total profit

        j = 0  # Pointer to iterate through the sorted jobs
        # Step 3: Iterate through each worker's ability
        for w in worker:
            # Step 4: Find the highest profit job this worker can do
            while j < len(jobs) and jobs[j][0] <= w:
                print(jobs[j], max_profit, total_profit)
                max_profit = max(max_profit, jobs[j][1])
                j += 1

            # Step 5: Add the best possible profit for this worker to the total profit
            total_profit += max_profit

        return total_profit
