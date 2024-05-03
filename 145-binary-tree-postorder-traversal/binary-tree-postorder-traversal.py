# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        # recursion
        def helperFunc(root):
            # base-case
            if not root:
                return

            helperFunc(root.left)
            helperFunc(root.right)
            answer.append(root.val)
        
        helperFunc(root)
        return answer

        