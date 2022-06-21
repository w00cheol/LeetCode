class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        answer = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                answer += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        return answer