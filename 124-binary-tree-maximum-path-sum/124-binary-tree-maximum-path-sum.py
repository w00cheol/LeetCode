class Solution:
    memorize = -2e9
    def includeRoot(self, root):
        if not root: return -2e9
        M_left, M_right = self.includeRoot(root.left), self.includeRoot(root.right)
        include_root = max(root.val, root.val + max(M_left, M_right))
        self.memorize = max(self.memorize, include_root, M_left + root.val + M_right)
        return include_root
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.includeRoot(root), self.memorize)