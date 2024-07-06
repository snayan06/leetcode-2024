class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        flag = 1
        # 1 for the LTR , and -1 for RTL
        direction = 1 
        for i in range(time):
            flag += direction
            if flag == n:
                direction = -1
            elif flag == 1:
                direction = 1
        
        return flag

