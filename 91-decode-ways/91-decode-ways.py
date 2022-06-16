class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        answer = [1, 1] + [0 for _ in range(len(s)-1)]
        for i in range(1, len(s)):
            if s[i] >= '1' and s[i] <= '9':
                answer[i+1] += answer[i]
            if s[i-1:i+1] >= '10' and s[i-1:i+1] <= '26':
                answer[i+1] += answer[i-1]
        return answer[-1]