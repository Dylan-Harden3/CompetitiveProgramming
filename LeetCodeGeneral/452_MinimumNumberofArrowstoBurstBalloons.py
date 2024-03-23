class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        s, e = points[0]

        for curS, curE in points[1:]:
            if e < curS:
                s, e = curS, curE
                res += 1
            else:
                s, e = (max(s, curS), min(e, curE))
        res += 1
        return res
