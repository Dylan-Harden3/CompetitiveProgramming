class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1: return 1
        trustCounts = defaultdict(int)

        trustsSomeone = set()
        for a, b in trust:
            trustCounts[b] += 1
            trustsSomeone.add(a)

        for k, v in trustCounts.items():
            if v == n-1 and k not in trustsSomeone:
                return k
        
        return -1
