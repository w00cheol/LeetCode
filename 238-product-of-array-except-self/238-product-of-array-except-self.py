class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        zero_index = zero = 0
        mul = 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                zero_index = i
            else: mul *= nums[i]
                
        if zero > 1:
            answer = [0 for _ in range(len(nums))]
            return answer
        
        elif zero == 1:
            for _ in range(len(nums)):
                answer.append(0)
            answer[zero_index] = mul
            return answer
        
        else:
            for i in range(len(nums)):
                answer.append(mul//nums[i])
            return answer