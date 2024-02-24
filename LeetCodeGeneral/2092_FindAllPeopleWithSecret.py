class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        adj = {}

        for src, dst, time in meetings:
            if time not in adj:
                adj[time] = defaultdict(list)

            adj[time][dst].append(src)
            adj[time][src].append(dst)

        def dfs(node, adj):
            if node in visited:
                return
            secrets.add(node)
            visited.add(node)
            for nei in adj[node]:
                dfs(nei, adj)

        for time in sorted(adj.keys()):
            visited = set()
            for src in adj[time].keys():
                if src in secrets:
                    dfs(src, adj[time])

        return list(secrets)
