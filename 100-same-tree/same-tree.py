from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees are identical.

        Args:
        - p (TreeNode): The root node of the first binary tree.
        - q (TreeNode): The root node of the second binary tree.

        Returns:
        - bool: True if the two binary trees are identical, False otherwise.

        Intuition:
        To determine if two binary trees are identical, we can perform a depth-first search (DFS) traversal
        simultaneously on both trees. At each step, we compare the corresponding nodes of the two trees.
        If the values of the current nodes are equal and their left and right subtrees are also identical,
        then the two trees are identical. Otherwise, they are not identical.

        Time Complexity:
        The time complexity is O(min(m, n)), where m and n are the numbers of nodes in the two binary trees.
        This is because we traverse each node of both trees once, and the traversal stops as soon as we find a mismatch.

        Space Complexity:
        The space complexity is O(min(h1, h2)), where h1 and h2 are the heights of the two binary trees.
        This is because the space used by the call stack during recursion is proportional to the height of the shallower tree.
        """

        def helperFunc(p, q):
            if not p and not q:
                return True

            if (
                not p or not q
            ):  # If one node is None while the other is not, or vice versa
                return False

            if p.val != q.val:  # If values of the current nodes are different
                return False

            # Recursively check the left and right subtrees
            return helperFunc(p.left, q.left) and helperFunc(p.right, q.right)

        return helperFunc(p, q)
