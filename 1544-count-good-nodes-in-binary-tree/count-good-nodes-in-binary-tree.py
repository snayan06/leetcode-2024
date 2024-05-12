class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Counts the number of "good" nodes in a binary tree.

        A "good" node is defined as a node in which the value of the node is greater than
        or equal to the maximum value along the path from the root to that node.

        Intuition:
        Perform a Depth-First Search (DFS) traversal of the binary tree while keeping track
        of the maximum value encountered along the path from the root to each node. If the
        value of a node is greater than or equal to the maximum value along its path, it is
        considered a "good" node, and the count is incremented.

        Args:
        - root: The root node of the binary tree.

        Returns:
        An integer representing the count of "good" nodes in the binary tree.

        Time Complexity:
        O(N), where N is the number of nodes in the binary tree.
        Each node is visited once during the Depth-First Search traversal.

        Space Complexity:
        O(H), where H is the height of the binary tree.
        The recursion stack space used is proportional to the height of the tree.
        """

        self.answer = 0  # Initialize the count of "good" nodes

        def helperFunc(root, maximum):
            if not root:
                return

            if root.val >= maximum:
                maximum = root.val
                self.answer += 1  # Increment the count of "good" nodes

            helperFunc(root.left, maximum)
            helperFunc(root.right, maximum)

        helperFunc(
            root, float("-inf")
        )  # Start the recursion with initial maximum as negative infinity

        return self.answer  # Return the count of "good" nodes
