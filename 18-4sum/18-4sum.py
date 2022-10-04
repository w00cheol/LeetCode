class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        nums.sort()
        
        for i in range(len(nums)-3):
            if nums[i] * 4 > target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, len(nums)-2):
                if nums[i] + nums[j] * 3 > target:
                    continue
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
        
                two_sum_target = target - nums[i] - nums[j]
            
                l = j + 1
                r = len(nums)-1
                
                while l < r:
                    if nums[l] + nums[r] == two_sum_target:
                        answer.add((nums[i], nums[j], nums[l], nums[r]))
                        l = l + 1
                    elif nums[l] + nums[r] < two_sum_target:
                        l = l + 1
                    else:
                        r = r - 1
            
        return answer