class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        left = 0
        right = len(people) - 1
        while left <= right:
            if left == right:
                ans += 1
                break 
            x = people[left]
            y = people[right]
            print(f"x:{x},y:{y}")
            print(f"left:{left},right:{right}")
            if x + y <= limit:
                left += 1
                right -= 1
                ans += 1
                continue
            if people[left] <= people[right]:
                ans += 1
                right -= 1
                continue
            else:
                ans += 1
                left += 1
        
        return ans
