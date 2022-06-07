class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        for i in range(1, n+1):
            if i%2:
                answer.append(answer[i-1]+1)
            else:
                answer.append(answer[i//2])
        return answer