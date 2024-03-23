class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))

        cache = {}
        def dfs(i):
            if i >= len(jobs):
                return 0
            if i in cache:
                return cache[i]
            res = dfs(i+1)
            n = bisect.bisect_left(jobs, jobs[i][1], key=lambda x: x[0])
            res = max(dfs(n) + jobs[i][2], res)
            cache[i] = res
            return res

        return dfs(0)
