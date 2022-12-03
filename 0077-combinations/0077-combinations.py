class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def dfs(arr, start_num, cnt):
            if cnt == 0:
                answer.append(arr)
                return
                
            for i in range(start_num, n - cnt + 2):
                dfs(arr + [i], i + 1, cnt - 1)
            
            
        dfs([], 1, k)
        
        return answer