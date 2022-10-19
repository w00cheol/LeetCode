class Solution:
    def restoreIpAddresses(self, s):
        answer = []
        
        def dfs(dot, fixed_s, remain_s):
            if dot + len(remain_s) < 4:
                return
            
            if dot == 3:
                if remain_s[0] == '0' and len(remain_s) > 1:
                    return
                elif int(remain_s) <= 255:
                    answer.append(fixed_s + remain_s)
                    return
            elif remain_s[0] == '0':
                dfs(dot + 1, fixed_s + remain_s[0] + '.', remain_s[1:])
            else:
                for i in range(3):
                    if int(remain_s[:i+1]) <= 255:
                        dfs(dot + 1, fixed_s + remain_s[:i+1] + '.', remain_s[i+1:])
            return
            
        dfs(0, "", s)
        return answer