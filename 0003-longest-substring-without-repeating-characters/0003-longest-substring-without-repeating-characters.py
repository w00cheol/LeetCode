class Solution:
    def lengthOfLongestSubstring(self, s):
        answer = 0
        idx_memory = dict()
        l = 0
        
        for r in range(len(s)):
            if s[r] in idx_memory and idx_memory[s[r]] >= l:
                l = idx_memory[s[r]] + 1
            else:
                answer = max(answer, r - l + 1)
                
            idx_memory[s[r]] = r
            
        return answer