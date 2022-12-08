class Solution:
    def addBinary(self, a, b):
        answer = ''
        i, j, cin = len(a) - 1, len(b) - 1, 0
        
        while i >= 0 and j >= 0:
            sum = int(a[i]) ^ int(b[j]) ^ cin
            cin = (int(a[i]) & int(b[j])) | (int(a[i]) & cin) | (int(b[j]) & cin)

            i -= 1
            j -= 1
            answer += str(sum)
            
        while i >= 0:
            sum = int(a[i]) ^ cin
            cin = int(a[i]) & cin
            
            i -= 1
            answer += str(sum)
        
        while j >= 0:
            sum = int(b[j]) ^ cin
            cin = int(b[j]) & cin
            
            j -= 1
            answer += str(sum)
            
        if cin: answer += str(cin)
        
        return answer[::-1]