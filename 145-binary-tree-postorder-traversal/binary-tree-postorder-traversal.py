# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        # # recursion
        # def helperFunc(root):
        #     # base-case
        #     if not root:
        #         return

        #     helperFunc(root.left)
        #     helperFunc(root.right)
        #     answer.append(root.val)

        # helperFunc(root)
        # return answer
        stack = []
        if not root:
            return answer
        stack.append(root)
        while stack:
            front_node = stack.pop()
            answer.append(front_node.val)

            if front_node.left:
                stack.append(front_node.left)
            if front_node.right:
                stack.append(front_node.right)
        # answer.reverse()
        answer = answer[::-1]
        return answer
