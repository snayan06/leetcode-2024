class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Calculates the total score in a game based on a list of operations.

        The game is played with a list of strings representing operations, where:
        - "C": Represents the last valid round's score should be removed.
        - "D": Represents doubling the last valid round's score.
        - "+": Represents adding the last two valid round's scores.
        - Integer: Represents a valid round's score.

        The method iterates through the operations, updating the record of valid
        scores accordingly. It then calculates and returns the total score.

        Parameters:
        - operations (List[str]): A list of strings representing the operations in the game.

        Returns:
        - int: The total score achieved in the game.
        """
        record = []
        for opr in operations:
            if opr == "C":
                record.pop()
            elif opr == "D":
                record.append(record[-1] * 2)
            elif opr == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(opr))
        
        total_score = sum(record)
        return total_score
