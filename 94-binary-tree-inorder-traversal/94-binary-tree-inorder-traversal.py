class Solution:
    answer = []
    def inorder(self, root):
        if root is None: return
        self.inorder(root.left)
        self.answer.append(root.val)
        self.inorder(root.right)
    def inorderTraversal(self, root):
        self.answer = []
        self.inorder(root)
        return self.answer