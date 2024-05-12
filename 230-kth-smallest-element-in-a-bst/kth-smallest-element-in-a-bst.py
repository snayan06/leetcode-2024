class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the kth smallest element in a binary search tree (BST).

        Approach 1: In-Order Traversal
        Perform an in-order traversal of the BST to collect all node values. Return the kth element from the sorted list of values.

        Time Complexity: O(N)
        Space Complexity: O(N)

        Approach 2: Iterative In-Order Traversal with Stack
        Perform an iterative in-order traversal of the BST using a stack. Track the current node and a stack to simulate recursion.
        When the kth smallest element is found, return its value.

        Time Complexity: O(H + k)
        Space Complexity: O(H)
        """

        # # Approach 1: In-Order Traversal
        # path = []

        # def helperFunc(node):
        #     if not node:
        #         return
        #     helperFunc(node.left)
        #     path.append(node.val)
        #     helperFunc(node.right)

        # helperFunc(root)
        # return path[k - 1]

        # Approach 2: Iterative In-Order Traversal with Stack
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
