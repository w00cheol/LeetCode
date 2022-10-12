class Solution:
    def countAndSay(self, n: int):
        answer = ['1']
        
        def countDigit(n):
            say = ''
            digit = n[0]
            count = 0
            
            for i in range(len(n)):
                if digit == n[i]:
                    count += 1
                else:
                    say = say + str(count) + digit
                    digit = n[i]
                    count = 1
                    
            return say + str(count) + digit
            
        for i in range(n-1):
            answer.append(countDigit(str(answer[-1])))
        
        return answer[-1]