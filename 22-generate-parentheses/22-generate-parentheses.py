class Solution:
    def generateParenthesis(self, n):
        
        def dfs(string, popen, pclose, answer):
            if pclose == 0:
                answer.append(string)
                
            if popen > 0:
                dfs(string + '(', popen-1, pclose, answer)
                
            if pclose > popen:
                dfs(string + ')', popen, pclose-1, answer)
                
            return answer
        
        return dfs('', n, n, [])