class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_map = {}

        sorted_scores = sorted(score, reverse=True)
        for i in range(len(sorted_scores)):
            s = sorted_scores[i]
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)

        return [rank_map[score[i]] for i in range(len(sorted_scores))]
