class Solution:
    def canJump(self, nums: List[int]) -> bool:
        M = 0
        for i in range(len(nums)):
            if i <= M:
                if i + nums[i] >= M:
                    M = i + nums[i]
                    if M >= len(nums)-1:
                        return True
            else:
                return False
                