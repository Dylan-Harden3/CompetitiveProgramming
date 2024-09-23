class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1
        
        return res

