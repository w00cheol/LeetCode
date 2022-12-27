class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum):
            if not root:
                return False
            
            if root.val == targetSum and not root.left and not root.right:
                return True
            
            if dfs(root.left, targetSum - root.val):
                return True
            
            if dfs(root.right, targetSum - root.val):
                return True
            
            return False
        
        return dfs(root, targetSum)