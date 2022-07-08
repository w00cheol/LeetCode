class Solution:
    def dfs(self, root, subRoot):
        if not root and not subRoot: return True
        if not root: return False
        if not subRoot: return False
        if root.val != subRoot.val: return False
        if self.dfs(root.left, subRoot.left) == False: return False
        if self.dfs(root.right, subRoot.right) == False: return False
        return True
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.dfs(root, subRoot) == True: return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)