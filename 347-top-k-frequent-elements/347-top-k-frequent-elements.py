from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        srtd = sorted(zip(dic, dic.values()), key=lambda x: x[1])
        answer = []
        for _ in range(k):
            answer.append(srtd.pop()[0])
        return answer