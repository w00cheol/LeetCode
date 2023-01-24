class Solution:
    def isSymmetric(self, root):
        def dfs(node_l, node_r):
            if node_l is None and node_r is None:
                return True
            
            if node_l is None or node_r is None:
                return False
            
            if node_l.val == node_r.val:
                return dfs(node_l.right, node_r.left) and dfs(node_l.left, node_r.right)
            else:
                return False
            
        return dfs(root.left, root.right)