class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        answer = ''
        cin = 0
        bitmask = 0
        
        while i >= 0 and j >= 0:
            sum = int(a[i]) + int(b[j]) + cin
            
            if sum >= 2:
                cin = 1
                sum -= 2
            else:
                cin = 0

            i -= 1
            j -= 1
            
            answer += str(sum)
            
        while i >= 0:
            sum = int(a[i]) + cin
            if sum == 2:
                cin = 1
                sum = 0
            else:
                cin = 0
                
            i -= 1
            answer += str(sum)
        
        while j >= 0:
            sum = int(b[j]) + cin
            if sum == 2:
                cin = 1
                sum = 0
            else:
                cin = 0
                
            j -= 1
            answer += str(sum)
            
        answer += str(cin)
        
        return answer[::-1] if cin else answer[-2::-1]