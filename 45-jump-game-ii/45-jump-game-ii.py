class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = checkpoint = next_checkpoint = 0
        
        for i in range(len(nums)):
            next_checkpoint = max(next_checkpoint, i + nums[i])
            
            if len(nums) - 1 <= checkpoint:
                return answer
            elif i == checkpoint:
                answer += 1
                checkpoint = next_checkpoint
            
        return answer