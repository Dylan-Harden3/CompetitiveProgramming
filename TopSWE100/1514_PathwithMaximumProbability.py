class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, edge in enumerate(edges):
            u, v = edge
            adj[u].append((succProb[i], v))
            adj[v].append((succProb[i], u))

        visited = set()
        q = [(-1, start_node)]
        while q:
            p, node = heapq.heappop(q)
            visited.add(node)
            if node == end_node:
                return p*-1
            for prob, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(q, (p *prob, nei))
        return 0
