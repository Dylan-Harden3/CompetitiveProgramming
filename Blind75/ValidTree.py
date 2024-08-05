class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        def dfs(n, prev):
            if n in visit:
                return False
            
            visit.add(n)
            for nei in adj[n]:
                if nei != prev and nei in visit:
                    return True
                elif nei != prev and dfs(nei, n):
                    return True
            return False
        
        return not dfs(0, -1) and len(visit) == n
