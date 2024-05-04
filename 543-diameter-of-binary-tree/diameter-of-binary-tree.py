from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the diameter of a binary tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.

        Args:
        - root (TreeNode): The root node of the binary tree.

        Returns:
        - int: The diameter of the binary tree.

        Intuition:
        We perform a depth-first search (DFS) traversal of the binary tree and calculate the depth of each node.
        During the traversal, we keep track of the maximum diameter encountered so far.
        At each node, we recursively calculate the depth of its left and right subtrees.
        We also calculate the diameter passing through the current node as the sum of the depths of its left and right subtrees.
        We update the maximum diameter encountered so far if the diameter passing through the current node is greater.
        Finally, we return the maximum diameter encountered during the traversal.

        Time Complexity:
        The time complexity is O(n), where n is the number of nodes in the binary tree. This is because we visit each node once.

        Space Complexity:
        The space complexity is O(h), where h is the height of the binary tree. This is because the space used by the call stack during recursion
        is proportional to the height of the tree.
        """

        def helperFunc(root, d):
            if not root:
                return 0, d

            lh, d = helperFunc(root.left, d)
            rh, d = helperFunc(root.right, d)

            diameter_through_node = lh + rh
            d = max(d, diameter_through_node)
            return 1 + max(lh, rh), d

        _, d = helperFunc(root, 0)
        return d
