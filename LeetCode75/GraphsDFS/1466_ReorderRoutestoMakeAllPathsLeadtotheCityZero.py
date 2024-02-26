class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = { (a, b) for a, b in connections }
        neighbors = defaultdict(list)

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        minChanges = 0
        visited = set()
        def dfs(node):
            for nei in neighbors[node]:
                if nei in visited:
                    continue
                if (nei, node) not in adj:
                    nonlocal minChanges
                    minChanges += 1
                visited.add(nei)
                dfs(nei)
        visited.add(0)
        dfs(0)
        return minChanges
