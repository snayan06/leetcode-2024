class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for roid in asteroids:
            if roid > 0:
                stack.append(roid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] + roid == 0:
                        stack.pop()
                        break
                    elif stack[-1] + roid < 0:
                        stack.pop()
                        continue
                    else:
                        break
                else:
                    stack.append(roid)

        return stack
