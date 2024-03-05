class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        prevStart = points[0][0]
        prevEnd = points[0][1]
        
        for start, end in points:
            if start <= prevEnd:
                prevEnd = min(prevEnd, end)
            else:
                prevStart, prevEnd = start, end
                res += 1
        return res
