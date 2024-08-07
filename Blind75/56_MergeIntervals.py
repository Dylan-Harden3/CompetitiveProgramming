class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur = intervals[0]
        for start, end in intervals[1:]:
            if start > cur[1]:
                res.append(cur)
                cur = [start, end]
            elif start <= cur[1]:
                cur[1] = max(end, cur[1])
        res.append(cur)
        return res