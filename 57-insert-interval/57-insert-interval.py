class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []: return [newInterval]
        start = []
        middle = []
        end = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                start.append(interval)
            elif interval[0] > newInterval[1]:
                end.append(interval)
            else:
                middle.append(interval)
        if middle:
            return start + [[min(middle[0][0], newInterval[0]), max(middle[-1][1], newInterval[1])]] + end
        else:
            return start + [newInterval] + end