class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        ptr = 0
        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[ptr][1]:
                cnt += 1
                ptr = i

        return len(intervals)-cnt
