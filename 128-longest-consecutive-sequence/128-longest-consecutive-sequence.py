class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer, dic = 0, {}
        for i in range(len(nums)): # O(n)
            dic[nums[i]] = True
        keys = list(dic.keys()) # O(n)
        for i in range(len(keys)): # O(n)
            if dic[keys[i]] == True:
                cnt = 1
                left_index, right_index = keys[i]-1, keys[i]+1
                while dic.get(left_index, False):
                    dic[left_index] = False
                    left_index -= 1
                    cnt += 1
                while dic.get(right_index, False):
                    dic[right_index] = False
                    right_index += 1
                    cnt += 1
                answer = max(answer, cnt)
        return answer