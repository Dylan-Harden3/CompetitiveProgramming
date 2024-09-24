class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = inf
        adj = defaultdict(list)
        for n1, n2, price in flights:
            adj[n1].append((n2, price))

        q = deque([(0, src)])
        dist = [float('inf')] * n
        while q and k >= 0:
            print(q)
            l = len(q)
            for i in range(l):
                cost, cur = q.pop()
                for nei, price in adj[cur]:
                    if price + cost < dist[nei]:
                        q.appendleft((price+cost, nei))
                        dist[nei] = price+cost
            k -= 1
        return dist[dst] if dist[dst] != inf else -1
