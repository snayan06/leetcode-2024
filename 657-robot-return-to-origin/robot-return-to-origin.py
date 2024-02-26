class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {"d": 0, "u": 0, "l": 0, "r": 0}

        for move in moves:
            if move == "D":
                d["d"] += 1
            elif move == "U":
                d["u"] += 1
            elif move == "L":
                d["l"] += 1
            elif move == "R":
                d["r"] += 1
        print(d)
        return (d["d"] == d["u"]) and (d["r"] == d["l"])
