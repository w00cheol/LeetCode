class Solution:
    def reverse(self, x: int) -> int:
        temp = 0
        pn = 1
        if x<0:
            x= -x
            pn = -1
        while x > 0:
            temp = temp*10 + x%10
            x=x//10
            if temp > 2147483647: return 0
        return temp*pn