from collections import defaultdict
class Solution:
    def dfs(self, root, depth, answer_dict):
        if not root: return answer_dict
        answer_dict[depth].append(root.val)
        answer_dict = self.dfs(root.left, depth + 1, answer_dict)
        answer_dict = self.dfs(root.right, depth + 1, answer_dict)
        return answer_dict
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.dfs(root, 0, defaultdict(list)).values()