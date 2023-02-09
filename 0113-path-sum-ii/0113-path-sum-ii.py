class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return
        answer = []
        
        def dfs(node, arr, running_sum):
            arr.append(node.val)
            running_sum += node.val
            
            if not node.left and not node.right:
                if running_sum == targetSum:
                    answer.append(arr)
                return
            
            if node.left:
                dfs(node.left, arr[::], running_sum)
                
            if node.right:
                dfs(node.right, arr[::], running_sum)
                
        dfs(root, [], 0)
        
        return answer