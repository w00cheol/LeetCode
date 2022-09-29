class Solution:
    def subsets(self, nums: List[int]):
        answer = [[]]
        
        for num in nums:
            for i in range(len(answer)):
                answer.append(answer[i] + [num])
                
        return answer