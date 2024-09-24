class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2-x1)+ abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        heap = [(0, 0)]
        while len(visit) < len(points):
            cost, point = heapq.heappop(heap)
            if point in visit:
                continue
            visit.add(point)
            res += cost
            for cost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(heap, [cost, nei])
        return res
