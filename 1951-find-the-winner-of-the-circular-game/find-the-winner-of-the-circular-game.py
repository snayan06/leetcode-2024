class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = []
        for i in range(1,n+1):
            array.append(i)
        starting_position = 0
        position_to_be_removed = 0
        while len(array) > 1:
            for i in range(0,k-1):
                starting_position += 1
                if starting_position >= len(array):
                    starting_position = 0

            array.pop(starting_position)
            if starting_position >= len(array):
                starting_position=0
        
        return array[0]
        