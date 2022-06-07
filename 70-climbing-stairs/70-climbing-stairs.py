class Solution:
    dic = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.dic.keys():
            return self.dic[n]
        self.dic[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.dic[n]