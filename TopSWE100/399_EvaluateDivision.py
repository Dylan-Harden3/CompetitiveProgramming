class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, p in enumerate(equations):
            a, b = p
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        
        res = []
        for c, d in queries:
            if c not in adj or d not in adj:
                res.append(-1.0)
                continue
            elif c == d:
                res.append(1.0)
                continue
            found = False
            visit = set()
            stack = [(c, 1.0)]
            while stack:
                cur, weight = stack.pop()
                visit.add(cur)
                if cur == d:
                    res.append(weight)
                    found = True
                    break
                for nei, w in adj[cur]:
                    if nei not in visit:
                        stack.append((nei, weight * w))
            if not found: res.append(-1.0)
        return res