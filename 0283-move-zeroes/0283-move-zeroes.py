class Solution:
    def moveZeroes(self, nums: List[int]):
        runner, zero_pointer = 0, 0
        
        while runner < len(nums):
            if nums[runner] != 0:
                nums[runner], nums[zero_pointer] = nums[zero_pointer], nums[runner]
                zero_pointer += 1
            
            runner += 1