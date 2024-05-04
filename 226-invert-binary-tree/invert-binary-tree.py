from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree recursively.

        Args:
        - root (TreeNode): The root node of the binary tree to be inverted.

        Returns:
        - TreeNode: The root node of the inverted binary tree.

        Intuition:
        To invert a binary tree, we need to swap the left and right subtrees of each node.
        We can achieve this recursively by traversing the tree and swapping the left and right subtrees of each node.

        Time Complexity:
        The time complexity is O(n), where n is the number of nodes in the binary tree. 
        This is because we visit each node once during the traversal.

        Space Complexity:
        The space complexity is O(h), where h is the height of the binary tree. 
        This is because the space used by the call stack during recursion is proportional to the height of the tree.
        """
        def helperFunc(root):
            if not root:
                return 
            
            # Swap left and right subtrees
            root.left, root.right = root.right, root.left
            
            # Recursively invert left and right subtrees
            helperFunc(root.left)
            helperFunc(root.right)

        helperFunc(root)
        return root
