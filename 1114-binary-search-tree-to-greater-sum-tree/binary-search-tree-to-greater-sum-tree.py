# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverseInorderTraversal(node,running_sum=0):
            if node:
                running_sum = reverseInorderTraversal(node.right,running_sum)
                running_sum += node.val
                node.val = running_sum
                running_sum = reverseInorderTraversal(node.left,running_sum)
            return running_sum

        reverseInorderTraversal(root)

        return root

