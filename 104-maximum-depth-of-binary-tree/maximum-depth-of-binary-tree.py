# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helperFunc(root):
            # base case
            if not root:
                return 0

            lh = helperFunc(root.left)
            rh = helperFunc(root.right)

            return 1 + max(lh, rh)

        return helperFunc(root)
