class Solution:
    def searchRange(self, nums, target):
        def findLeft(nums, target):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l+r) // 2
                
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return l
            
        def findRight(nums, target):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                mid = (l+r) // 2
                
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                
            return r
        
        left, right = findLeft(nums, target), findRight(nums, target)
        
        return [left, right] if left <= right else [-1, -1]