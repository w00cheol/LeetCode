class Solution:
    def reverseBits(self, n) -> int:
        answer = n & 1
        
        for _ in range(31):
            answer <<= 1
            n >>= 1
            
            answer |= (n & 1)
        
        return answer