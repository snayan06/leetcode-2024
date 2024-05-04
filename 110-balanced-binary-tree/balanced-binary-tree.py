from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines whether a binary tree is balanced.

        Args:
        - root (TreeNode): The root node of the binary tree.

        Returns:
        - bool: True if the binary tree is balanced, False otherwise.

        Intuition:
        A binary tree is considered balanced if the heights of its left and right subtrees differ by at most 1,
        and both the left and right subtrees are also balanced.

        We use a recursive approach to calculate the height of each subtree and check if it is balanced.
        At each node, we recursively calculate the height of its left and right subtrees.
        If any subtree is found to be unbalanced, or if the difference in heights of left and right subtrees
        exceeds 1, then the entire tree is unbalanced.

        Time Complexity:
        The time complexity is O(n), where n is the number of nodes in the binary tree. This is because we visit each node once.

        Space Complexity:
        The space complexity is O(h), where h is the height of the binary tree. This is because the space used by the call stack during recursion
        is proportional to the height of the tree.
        """

        def helperFunc(root):
            if not root:
                return 0, True

            lh, lb = helperFunc(root.left)
            if not lb:
                return 0, False

            rh, rb = helperFunc(root.right)
            if not rb:
                return 0, False

            height = 1 + max(lh, rh)
            balanced = abs(lh - rh) <= 1

            return height, balanced

        _, balanced = helperFunc(root)
        return balanced if balanced is not None else False
