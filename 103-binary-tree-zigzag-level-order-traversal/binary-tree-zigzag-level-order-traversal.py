from collections import deque
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Returns the zigzag level order traversal of a binary tree.

        Intuition:
        Perform a level order traversal of the binary tree using a queue. Use a flag to toggle between left-to-right
        and right-to-left traversal for each level. At each level, reverse the order of nodes if the traversal is
        from right to left. Store the values of nodes in each level in a list and append them to the answer.

        Args:
        - root: The root node of the binary tree.

        Returns:
        A list of lists containing the zigzag level order traversal of the binary tree.

        Time Complexity:
        O(N), where N is the number of nodes in the binary tree. Each node is visited once during the level order traversal.

        Space Complexity:
        O(N), where N is the number of nodes in the binary tree. The space complexity is dominated by the queue used for
        level order traversal and the answer list containing the zigzag level order traversal.
        """

        answer = []
        if not root:
            return answer

        q = deque()
        q.append(root)
        left_to_right = (
            True  # Flag to indicate left-to-right traversal or right-to-left traversal
        )

        while q:
            size = len(q)
            level = [0] * size

            for i in range(size):
                node = q.popleft()

                # Determine the index based on the traversal direction
                index = i if left_to_right else size - 1 - i

                # Store the value of the node at the appropriate index
                level[index] = node.val

                # Enqueue the left and right children if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Toggle the traversal direction for the next level
            left_to_right = not left_to_right
            answer.append(level)

        return answer
