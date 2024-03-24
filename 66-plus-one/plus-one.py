class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits into a single integer
        num = 0
        for digit in digits:
            print(num,digit)
            num = num * 10 + digit
            print(num)
        
        # Add 1 to the integer
        num += 1
        
        # Convert the resulting integer back into a list of digits
        result = []
        while num > 0:
            result.insert(0, num % 10)
            num = num // 10
        
        return result