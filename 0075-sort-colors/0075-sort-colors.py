class Solution:
    def sortColors(self, nums) -> None:
        dic = {0: 0, 1:0, 2:0}
        
        for num in nums:
            dic[num] += 1
        
        i = 0
        for _ in range(dic[0]):
            nums[i] = 0
            i += 1
        for _ in range(dic[1]):
            nums[i] = 1
            i += 1
        for _ in range(dic[2]):
            nums[i] = 2
            i += 1