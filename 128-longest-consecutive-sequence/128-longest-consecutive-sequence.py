class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer, dic = 0, {}
        for i in range(len(nums)): # O(n)
            dic[nums[i]] = True
        keys = list(dic.keys()) # O(n)
        for i in range(len(keys)): # O(n)
            if keys[i] in dic: # O(1)
                cnt = 1
                left_index, right_index = keys[i]-1, keys[i]+1
                while left_index in dic: # O(1)
                    cnt += 1
                    del dic[left_index]
                    left_index -= 1
                while right_index in dic: # O(1)
                    cnt += 1
                    del dic[right_index]
                    right_index += 1
                answer = max(answer, cnt)
        return answer