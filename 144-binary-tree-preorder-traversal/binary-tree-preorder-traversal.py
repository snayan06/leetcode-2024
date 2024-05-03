class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform preorder traversal of a binary tree recursively or iteratively and return the node values.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            List[int]: A list containing node values in preorder traversal order.

        Intuition:
        - Preorder traversal visits each node in the binary tree in the order: root, left, right.
        
        Recursive Approach:
        - In the recursive approach:
            - We define a helper function to perform the traversal.
            - If the root is None (base case), we return from the function.
            - Otherwise, we append the value of the root node to the answer list.
            - Then, we recursively call the helper function for the left and right subtrees.
            - This results in a depth-first traversal of the tree.
        
        Iterative Approach:
        - In the iterative approach using a stack:
            - We start with an empty stack and push the root node onto the stack.
            - While the stack is not empty:
                - Pop a node from the stack and process it (add its value to the answer list).
                - Push the right child of the popped node onto the stack if it exists.
                - Push the left child of the popped node onto the stack if it exists.
                - By pushing the right child before the left child, we ensure that the left
                  child will be processed before the right child when popping from the stack.
                - This mimics the behavior of preorder traversal, where the left child is
                  processed before the right child.
            - Continue until the stack is empty.
        
        Time Complexity (TC):
        - The time complexity is O(N), where N is the number of nodes in the binary tree.
          We visit each node exactly once in both the recursive and iterative approaches.

        Space Complexity (SC):
        - Recursive Approach: The space complexity is O(N) due to the recursive call stack,
          where N is the height of the binary tree in the worst case.
        - Iterative Approach: The space complexity is O(N) due to the stack used for iteration,
          where N is the number of nodes in the binary tree.
        """
        # Recursive Approach
        def recursive_preorder(node):
            if not node:
                return
            answer.append(node.val)
            recursive_preorder(node.left)
            recursive_preorder(node.right)

        # Iterative Approach
        answer = []
        stack = []

        if not root:
            return answer
        
        stack.append(root)
        while stack:
            node = stack.pop()

            answer.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        # Call recursive approach
        # recursive_preorder(root)
        
        return answer
