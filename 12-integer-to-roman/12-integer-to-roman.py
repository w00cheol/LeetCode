class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        num = str(num)
        lenN = len(num)
        for i in range(len(num)):
            if num[i] == '4':
                if lenN == 3:
                    answer += 'CD'
                if lenN == 2:
                    answer += 'XL'
                if lenN == 1:
                    answer += 'IV'
                lenN -= 1
                continue
            elif num[i] == '9':
                if lenN == 3:
                    answer += 'CM'
                if lenN == 2:
                    answer += 'XC'
                if lenN == 1:
                    answer += 'IX'
                lenN -= 1
                continue
            now = int(num[i])
            if now >= 5:
                if lenN == 3:
                    answer += 'D'
                if lenN == 2:
                    answer += 'L'
                if lenN == 1:
                    answer += 'V'
                now -= 5
            if lenN == 4:
                answer += 'M'*now
            elif lenN == 3:
                answer += 'C'*now
            elif lenN == 2:
                answer += 'X'*now
            elif lenN == 1:
                answer += 'I'*now
            lenN -= 1
        return answer