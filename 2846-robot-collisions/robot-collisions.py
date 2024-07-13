from typing import List
from collections import deque

class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        # Create a list of robot dictionaries
        robots = []
        for i in range(len(positions)):
            robot = {
                "position": positions[i],
                "health": healths[i],
                "direction": directions[i],
                "robot_rank": i,
            }
            robots.append(robot)

        # Sort robots by their positions
        robots.sort(key=lambda x: x["position"])

        # Use a deque to manage right-moving robots
        deque_stack = deque()

        for robot in robots:
            if robot["direction"] == "R":
                deque_stack.append(robot)
            else:  # direction is 'L'
                while deque_stack and deque_stack[-1]["direction"] == "R":
                    last_robot = deque_stack[-1]
                    if last_robot["health"] == robot["health"]:
                        # Both robots destroy each other
                        deque_stack.pop()
                        robot["health"] = 0
                        break
                    elif last_robot["health"] > robot["health"]:
                        last_robot["health"] -= 1
                        robot["health"] = 0
                        break
                    else:
                        deque_stack.pop()
                        robot["health"] -= 1

                # If the robot still has health, it survives
                if robot["health"] > 0:
                    deque_stack.append(robot)

        # Collect surviving robots' healths
        survivors = [robot for robot in deque_stack if robot["health"] > 0]

        # Sort survivors by their original index
        survivors.sort(key=lambda x: x["robot_rank"])
        return [robot["health"] for robot in survivors]



