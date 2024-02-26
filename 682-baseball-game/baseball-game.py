class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for opr in operations:
            if opr == "C":
                record.pop()
            elif opr == "D":
                record.append(record[-1]*2)
            elif opr == "+":
                record.append(record[-1]+record[-2])
            else:
                record.append(int(opr))
        s = 0
        for r in record:
            s+=r
        
        return s



        