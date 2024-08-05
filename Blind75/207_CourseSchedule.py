class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[b].append(a)

        visit = defaultdict(int)
        def hasCycle(v):
            if visit[v] == 2:
                return False
            
            visit[v] = 1
            for nei in adj[v]:
                if visit[nei] == 1:
                    return True
                elif visit[nei] == 2:
                    continue
                elif hasCycle(nei):
                    return True
            visit[v] = 2
            return False
        
        for v in range(numCourses):
            if hasCycle(v): return False
        return True