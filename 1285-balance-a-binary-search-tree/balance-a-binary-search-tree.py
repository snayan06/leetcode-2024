# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Balance a given Binary Search Tree (BST) by performing an inorder traversal
        to obtain the sorted elements and then reconstructing the tree in a balanced manner.

        :param root: TreeNode, the root of the BST to be balanced
        :return: TreeNode, the root of the balanced BST
        """
        sorted_elements = []

        def inorder_traversal(node):
            """
            Perform inorder traversal on the BST to collect elements in sorted order.

            :param node: TreeNode, current node in the BST
            """
            if node:
                inorder_traversal(node.left)
                sorted_elements.append(node.val)
                inorder_traversal(node.right)

        def build_balanced_bst(elements):
            """
            Build a balanced BST from a sorted array of elements.

            :param elements: List[int], sorted array of BST elements
            :return: TreeNode, the root of the balanced BST
            """
            if not elements:
                return None
            mid = len(elements) // 2
            root = TreeNode(val=elements[mid])
            root.left = build_balanced_bst(elements[:mid])  # Elements before mid
            root.right = build_balanced_bst(elements[mid + 1 :])  # Elements after mid
            return root

        # Perform inorder traversal to get sorted elements
        inorder_traversal(root)

        # Construct a balanced BST from the sorted elements
        return build_balanced_bst(sorted_elements)
