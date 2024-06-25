# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        Transforms a Binary Search Tree (BST) into a Greater Sum Tree (GST) using reverse in-order traversal.

        Reverse in-order traversal (right, root, left) is effective here because:
        - It visits nodes in descending order of their values.
        - Updates each node's value to be the sum of itself and all nodes with values greater than it in the original BST.

        Args:
        - root (TreeNode): The root node of the BST.

        Returns:
        - TreeNode: The root node of the transformed Greater Sum Tree (GST).
        """

        def reverseInorderTraversal(node, running_sum=0):
            """
            Performs reverse in-order traversal of the BST and updates node values.

            Args:
            - node (TreeNode): Current node being processed.
            - running_sum (int): Cumulative sum of nodes greater than the current node.

            Returns:
            - int: Updated running_sum after processing the subtree rooted at 'node'.
            """
            if node:
                # Traverse right subtree
                running_sum = reverseInorderTraversal(node.right, running_sum)

                # Update node value with running_sum
                running_sum += node.val
                node.val = running_sum

                # Traverse left subtree
                running_sum = reverseInorderTraversal(node.left, running_sum)

            return running_sum

        # Start reverse in-order traversal from the root
        reverseInorderTraversal(root)

        return root
