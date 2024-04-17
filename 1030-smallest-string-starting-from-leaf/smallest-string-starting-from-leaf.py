# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path, paths):
        if not node:
            return
        path.append(chr(node.val + ord("a")))
        if not node.left and not node.right:  # Leaf node reached
            paths.append("".join(reversed(path)))  # Append path to the list
        else:
            self.dfs(node.left, path, paths)
            self.dfs(node.right, path, paths)

        path.pop()  # Backtrack: remove the current node from the path

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = []
        self.dfs(root, [], paths)
        return min(paths)
