class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for i, keys in enumerate(rooms):
            adj[i] = keys

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        dfs(0)
        return len(visited) == len(rooms)
