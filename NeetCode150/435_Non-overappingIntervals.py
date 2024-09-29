class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cur = intervals[0]
        res = 0
        for start, end in intervals[1:]:
            if start < cur[1]:
                res += 1
                cur[1] = min(cur[1], end)
            else:
                cur = [start, end]
        return res
