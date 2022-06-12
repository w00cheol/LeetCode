class Solution:
    def wordBreak(self, s, words):
        dp = [True] + [False for _ in range(len(s))]
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    continue
        return dp[-1]