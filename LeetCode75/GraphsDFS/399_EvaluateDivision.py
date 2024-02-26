class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, e in enumerate(equations):
            a, b = e
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))

        def dfs(src, tgt):
            if src not in adj or tgt not in adj:
                return -1.0
            stack = [(src, 1.0)]
            visited = set()
            while stack:
                curNode, curWeight = stack.pop()

                visited.add(curNode)
                if curNode == tgt:
                    return curWeight
                
                for nei, w in adj[curNode]:
                    if nei not in visited:
                        stack.append((nei, curWeight * w))
            return -1.0
        
        return [dfs(a, b) for a, b in queries]
