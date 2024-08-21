class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        cur = intervals[0]
        
        for start, end in intervals[1:]:
            if start < cur[1]:
                res += 1
                if end < cur[1]:
                    cur = [start, end]
            else:
                cur = [start, end]
        return res
