class Solution:
    def grayCode(self, n):
        return [i ^ i//2 for i in range(2**n)]