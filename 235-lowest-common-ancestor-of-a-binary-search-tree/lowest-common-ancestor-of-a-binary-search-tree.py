class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Intuition:
        - In a Binary Search Tree (BST), the left subtree of a node contains only nodes with values lesser than the node's value,
          and the right subtree contains only nodes with values greater than the node's value.
        - Therefore, the lowest common ancestor of nodes p and q would be the node where p and q are separated into different subtrees
          (or one of the nodes is the root itself).

        Time Complexity: O(h), where h is the height of the tree.
          - In the worst-case scenario, we may have to traverse the height of the tree.
        Space Complexity: O(1) if we disregard the recursion stack, otherwise O(h).
          - The space used by the recursion stack during the function calls is proportional to the height of the tree.
        """
        if not root:
            return None

        curr = root.val
        if curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root
