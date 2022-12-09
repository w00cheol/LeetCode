class Solution:
    def reverseBits(self, n):
        answer = n & 1
        
        for _ in range(32 - 1):
            answer <<= 1
            n >>= 1
            
            answer |= (n & 1)
        
        return answer