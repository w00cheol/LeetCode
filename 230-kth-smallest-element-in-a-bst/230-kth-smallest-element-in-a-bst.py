class Solution:
    def dfs(self, root, answer):
        if not root: return
        answer.append(root.val)
        self.dfs(root.left, answer)
        self.dfs(root.right, answer)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = []
        self.dfs(root, answer)
        return sorted(answer)[k-1]