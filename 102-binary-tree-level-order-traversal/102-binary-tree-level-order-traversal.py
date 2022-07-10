from collections import defaultdict
class Solution:
    def dfs(self, root, depth, answer):
        if not root: return answer
        answer[depth].append(root.val)
        self.dfs(root.left, depth + 1, answer)
        self.dfs(root.right, depth + 1, answer)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = defaultdict(list)
        self.dfs(root, 0, answer)
        return answer.values()