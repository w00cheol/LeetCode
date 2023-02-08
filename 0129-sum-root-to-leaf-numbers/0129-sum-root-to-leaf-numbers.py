class Solution:
    def sumNumbers(self, root):
        global answer
        answer = 0
        
        def dfs(running_sum, node):
            running_sum += node.val
            
            if not node.left and not node.right:
                global answer
                answer += running_sum
                return
            
            if node.left:
                dfs(running_sum * 10, node.left)
            if node.right:
                dfs(running_sum * 10, node.right)
                
        dfs(0, root)        
                
        return answer