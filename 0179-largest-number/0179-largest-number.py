class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(nums[x] + nums[y]) >= int(nums[y] + nums[x])
                
        nums = list(map(str, nums))
        
        for x in range(len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if compare(x, y) == False:
                    nums[x], nums[y] = nums[y], nums[x]
                    
        return "0" if nums[0] == '0' else ''.join(nums)