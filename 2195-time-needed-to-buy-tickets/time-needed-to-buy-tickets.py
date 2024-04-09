class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for index, ticket in enumerate(tickets):
            if index < k:
                count += min(tickets[k],tickets[index])
            elif index >k :
                count += min(tickets[k]-1,tickets[index])
            else:
                count += tickets[k]

        return count
            

            

        