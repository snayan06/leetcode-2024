class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        while numBottles - numExchange >= 0:
            answer += numBottles // numExchange
            numBottles = (numBottles // numExchange) + numBottles % numExchange
            print(numBottles, answer)

        return answer
