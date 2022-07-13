class Solution:
    def dfs(self, root, num):
        if root.left:
            num = self.dfs(root.left, num)
            if num == None:
                return None
        if num >= root.val:
            return None
        if root.right:
            num = self.dfs(root.right, root.val)
            if num == None:
                return None
            return num
        return root.val
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if self.dfs(root, -2**31-1) == None: return False
        return True