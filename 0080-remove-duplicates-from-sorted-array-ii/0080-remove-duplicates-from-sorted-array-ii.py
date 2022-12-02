class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        runner = 2
        
        for i in range(2, len(nums)):
            if nums[i] == nums[runner - 1] and nums[i] == nums[runner - 2]:
                    continue
                
            nums[runner] = nums[i]
            runner += 1
            
        return min(len(nums), runner)