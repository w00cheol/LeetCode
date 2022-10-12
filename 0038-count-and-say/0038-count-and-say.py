class Solution:
    def countAndSay(self, n: int) -> str:
        answer = ['1']
        
        def countDigit(n):
            say = ''
            count = 0
            digit = n[0]
            
            for i in range(len(n)):
                if digit == n[i]:
                    count += 1
                else:
                    say = say + str(count) + digit
                    digit = n[i]
                    count = 1
            
            say = say + str(count) + digit
            
            return say
            
        for i in range(n-1):
            answer.append(countDigit(str(answer[-1])))
        
        return answer[-1]