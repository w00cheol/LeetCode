class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def atoi(num):
            i = 0
            
            for n in num:
                i *= 10
                i += ord(n) - ord('0')
            
            return i

        return str(atoi(num1) * atoi(num2))