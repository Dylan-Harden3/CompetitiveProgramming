class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        adj = defaultdict(list)

        for src, dst, weight in times:
            adj[src].append((dst, weight))
        
        heap = [(0, k)]
        visit = set()
        res = 0
        while heap:
            cost, cur = heapq.heappop(heap)
            if cur in visit:
                continue
            res = cost
            visit.add(cur)
            for nei, weight in adj[cur]:
                if nei not in visit:
                    heapq.heappush(heap, (cost + weight, nei))
        return res if len(visit) == n else -1
