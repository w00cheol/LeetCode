class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        global prev, first, second
        prev, first, second = None, None, None
        
        def dfs(curr):
            global prev, first, second
            
            if curr is None:
                return None
            
            dfs(curr.left)
            
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                second = curr
            
            prev = curr
            dfs(curr.right)
        
        dfs(root)
        
        first.val, second.val = second.val, first.val