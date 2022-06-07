import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        for i in range(1, n+1):
            cnt = 0
            leftN = logN = i
            while leftN > 0:
                logN = math.trunc(math.log2(leftN))
                leftN -= 2**logN
                cnt += 1
            answer.append(cnt)
        return answer