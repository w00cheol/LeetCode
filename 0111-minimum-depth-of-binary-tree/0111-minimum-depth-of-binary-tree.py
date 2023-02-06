from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([[1, root]])
        
        while q:
            depth, node = q.popleft()
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                q.append([depth + 1, node.left])
                
            if node.right:
                q.append([depth + 1, node.right])