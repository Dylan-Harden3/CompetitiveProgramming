"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        res = 0
        s, e = 0, 0
        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                s += 1
                res = max(res, s-e)
            else:
                e += 1
        return res
