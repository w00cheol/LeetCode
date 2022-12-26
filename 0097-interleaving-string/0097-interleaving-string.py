class Solution:
    def isInterleave(self, s1, s2, s3):
        # Time complexity: O(n*m)
        # Space complexity: O(n*m)
        
        # I think I could optimize Space complexity to O(min(len(s1), len(s2)))
        # , using just one row (len = (min(len(s1), len(s2))))
        # and consider the stored index as an 1 level upper row index
        
        if len(s1) + len(s2) != len(s3): # impossible mission is given
            return False
        
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        
        # initialize dp array considering c = 0
        r = 1
        while r <= len(s1) and dp[r - 1][0] and s1[r - 1] == s3[r - 1]:
            dp[r][0] = True
            r += 1
        
        # initialize dp array considering r = 0
        c = 1
        while c <= len(s2) and dp[0][c - 1] and s2[c - 1] == s3[c - 1]:
            dp[0][c] = True
            c += 1
        
        # start dp algorithm
        for r in range(1, len(s1) + 1):
            for c in range(1, len(s2) + 1):
                use_s1 = dp[r - 1][c] and s1[r - 1] == s3[(r - 1) + c]
                use_s2 = dp[r][c - 1] and s2[c - 1] == s3[r + (c - 1)]
                
                dp[r][c] =  use_s1 or use_s2
                
        return dp[-1][-1]