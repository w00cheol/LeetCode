class Solution:
    def greedy(self, root, p, q):
        if root.val == p or root.val == q: return root
        if p < root.val < q: return root
        if root.val < p: return self.greedy(root.right, p, q)
        if q < root.val: return self.greedy(root.left, p, q)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.greedy(root, min(p.val, q.val), max(p.val, q.val))