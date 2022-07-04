class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
        if not root:
            return depth
        return max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1))