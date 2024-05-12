# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        path = []

        # Helper function for in-order traversal
        def helperFunc(node):
            if not node:
                return

            helperFunc(node.left)
            path.append(node.val)
            helperFunc(node.right)

        # Perform in-order traversal
        helperFunc(root)

        return path[k-1]
