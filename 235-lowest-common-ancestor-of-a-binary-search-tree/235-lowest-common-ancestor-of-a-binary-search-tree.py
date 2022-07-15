class Solution:
    def greedy(self, root, p, q):
        if root.val < p:
            return self.greedy(root.right, p, q)
        if q < root.val:
            return self.greedy(root.left, p, q)
        return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.greedy(root, min(p.val, q.val), max(p.val, q.val))