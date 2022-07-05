class Solution:
    def dfs(self, p, q):
        if p is None:
            if q is None: return True
            if q is not None: return False
        elif q is None: return False
        if p.val != q.val: return False
        if self.dfs(p.left, q.left) == False: return False
        if self.dfs(p.right, q.right) == False: return False
        return True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)