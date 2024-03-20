class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+2)]
        ms = [1] * (n+1)

        def union(a, b):
            x = find(a)
            y = find(b)
            if x == y:
                return

            if ms[x] > ms[y]:
                parent[y] = x
                ms[x] += ms[y]
            elif ms[y] >= ms[x]:
                parent[x] = y
                ms[y] += ms[x]
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            union(a, b)

