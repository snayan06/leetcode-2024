# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        # recursion
        def helperFunc(root):
            # base-case
            if not root:
                return

            helperFunc(root.left)
            answer.append(root.val)
            helperFunc(root.right)

        helperFunc(root)
        return answer
