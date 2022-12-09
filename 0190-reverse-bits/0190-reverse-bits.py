class Solution:
    def reverseBits(self, n):
        answer = 0
        
        for _ in range(32):
            answer = (answer << 1) | (n & 1)
            n >>= 1
            
        return answer