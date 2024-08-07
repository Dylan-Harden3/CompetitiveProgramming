class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                res.append(newInterval)
                res += intervals[i:]
                inserted = True
                break
            else:
                res.append(intervals[i])
        if not inserted:
            res.append(newInterval)
        
        sol = []
        cur = res[0]
        for start, end in res[1:]:
            if start > cur[1]:
                sol.append(cur)
                cur = [start, end]
            else:
                cur[1] = max(cur[1], end)
        sol.append(cur)
        return sol