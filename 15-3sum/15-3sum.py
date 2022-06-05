class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set([])
        p = []
        n = []
        z = []
        for i in range(len(nums)):
            if nums[i]>0: p.append(nums[i])
            if nums[i]<0: n.append(nums[i])
            if nums[i]==0: z.append(0)
        if len(z)>=3: answer.add((0,0,0))
        setN, setP = set(n), set(p)
        if len(z)>0:
            if len(setP) <= len(setN):
                for i in setP:
                    if -i in setN:
                        answer.add((-i, 0, i))
            else:
                for i in setN:
                    if -i in setP:
                        answer.add((-i, 0, i))
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if -(p[i]+p[j]) in setN:
                    answer.add((-(p[i]+p[j]), min(p[i], p[j]), max(p[i], p[j])))
                    continue
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if -(n[i]+n[j]) in setP:
                    answer.add((min(n[i], n[j]), max(n[i], n[j]), -(n[i]+n[j])))
                    continue
        return answer