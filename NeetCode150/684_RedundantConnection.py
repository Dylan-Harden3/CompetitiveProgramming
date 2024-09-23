class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(0, n+1)]
        max_size = [1]*(n+1)

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            x, y = find(a), find(b)
            if x == y:
                return
            
            if max_size[x] > max_size[y]:
                parent[y] = x
                max_size[x] += 1
            else:
                parent[x] = y
                max_size[y] += 1
        
        for n1, n2 in edges:
            if find(n1) == find(n2):
                return [n1, n2]
            union(n1, n2)

