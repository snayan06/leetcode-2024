class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines whether a binary tree is a valid binary search tree (BST).

        A binary tree is a valid BST if, for each node, the values in the left subtree are less than the node's value,
        and the values in the right subtree are greater than the node's value. Additionally, each subtree must also be
        a valid BST.

        Intuition:
        Perform an in-order traversal of the binary tree to obtain a sorted list of node values. If the resulting list
        is sorted in ascending order, the tree is a valid BST.

        Args:
        - root: The root node of the binary tree.

        Returns:
        A boolean value indicating whether the binary tree is a valid BST.

        Time Complexity:
        O(N), where N is the number of nodes in the binary tree. This is because we need to traverse each node once
        during the in-order traversal.

        Space Complexity:
        O(N), where N is the number of nodes in the binary tree. This is because we use an additional list (path) to store
        the values of the nodes during traversal.
        """

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

        # Check if the resulting list is sorted in ascending order
        for i in range(len(path) - 1):
            if path[i] >= path[i + 1]:
                return False

        return True
