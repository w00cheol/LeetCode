class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, 46340
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid * mid <= x:
                l = mid + 1
            else:
                r = mid - 1
            
        return r