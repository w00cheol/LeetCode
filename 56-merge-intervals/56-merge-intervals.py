class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        answer = [[intervals[0][0], intervals[0][1]]]
        for i in range(1, len(intervals)):
            if answer[-1][1] >= intervals[i][0]:
                if intervals[i][1] < answer[-1][0]:
                    answer.append(intervals[i])
                else:
                    answer[-1][0] = min(answer[-1][0], intervals[i][0])
                    answer[-1][1] = max(answer[-1][1], intervals[i][1])
            else:
                answer.append(intervals[i])
        return answer