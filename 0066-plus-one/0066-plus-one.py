class Solution:
    def plusOne(self, digits: List[int]):
        target = len(digits) - 1
        
        while target >= 0 and digits[target] == 9:
            digits[target] = 0
            target -= 1
        
        if target == -1:
            return [1] + digits
        else:
            digits[target] += 1
            return digits