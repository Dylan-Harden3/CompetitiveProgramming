class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        res = []
        cur = intervals[0]
        for start, end in intervals[1:]:
            if start <= cur[1]:
                cur[1] = max(cur[1], end)
            else:
                res.append(cur)
                cur = [start, end]
        res.append(cur)
        return res
