from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)
