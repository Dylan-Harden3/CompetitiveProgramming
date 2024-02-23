class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for start, end, price in flights:
            adj[start].append([end, price])

        queue = deque()
        queue.append((src, 0))

        dist = {}
        for i in range(n):
            dist[i] = inf
        
        dist[src] = 0

        while queue and k >= 0:
            s = len(queue)
            for i in range(s):
                cur, price = queue.pop()

                for neighbor, p in adj[cur]:
                    if price + p < dist[neighbor]:
                        dist[neighbor] = price + p
                        queue.appendleft((neighbor, price + p))
            k -= 1
        
        return dist[dst] if dist[dst] != inf else -1
