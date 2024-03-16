class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        low, high = intervals[0]
        res = []
        for l, h in intervals[1:]:
            if l > high:
                res.append([low, high])
                low, high = l, h
            elif l <= high:
                high = max(h, high)
        res.append([low, high])
        return res
