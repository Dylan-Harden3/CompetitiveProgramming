"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.end)
        cur = intervals[0]
        for interval in intervals[1:]:
            if interval.start < cur.end:
                return False
            cur = interval
        return True
