class Solution:
    def dfs(self, root, answer):
        if root == None: return None
        self.dfs(root.left, answer)
        self.dfs(root.right, answer)
        answer.append(root.val)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int):
        answer = []
        self.dfs(root, answer)
        return sorted(answer)[k-1]