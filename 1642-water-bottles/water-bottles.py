class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrankBottles = numBottles
        while numBottles >= numExchange:
            newFullBottles = numBottles // numExchange
            remainingEmptyBottles = numBottles % numExchange
            totalDrankBottles += newFullBottles
            numBottles = newFullBottles + remainingEmptyBottles
            print(numBottles, totalDrankBottles)

        return totalDrankBottles