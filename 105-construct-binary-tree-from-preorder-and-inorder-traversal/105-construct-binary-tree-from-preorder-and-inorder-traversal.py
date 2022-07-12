class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        cut_right = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:cut_right+1], inorder[:cut_right])
        root.right = self.buildTree(preorder[cut_right+1:], inorder[cut_right+1:])
        return root