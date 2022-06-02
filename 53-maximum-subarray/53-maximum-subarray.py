class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            start = max(start+nums[i], nums[i])
            answer = max(answer, start)
        return answer 
    
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.__div_conquer(nums, 0, len(nums)-1)
    
    def __div_conquer(self, nums, left, right):
        if left > right:
            return -2e9
        mid = (left+right)//2
        max_left = sum_left = max_right = sum_right = 0
        for i in range(mid-1, left-1, -1):
            sum_left += nums[i]
            max_left = max(max_left, sum_left)
        for i in range(mid+1, right+1):
            sum_right += nums[i]
            max_right = max(max_right, sum_right)
        
        now = max_left + max_right + nums[mid]
        div_left = self.__div_conquer(nums, left, mid-1)
        div_right = self.__div_conquer(nums, mid+1, right)
        
        return max(div_left, div_right, now)
'''