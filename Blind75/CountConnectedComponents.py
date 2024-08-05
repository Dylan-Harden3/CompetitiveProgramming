class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ms = [0] * n
        parent = [i for i in range(n)]

        def find(a):
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            x = find(a)
            y = find(b)

            if x == y:
                return
            
            if ms[x] > ms[y]:
                parent[y] = x
                ms[x] += 1
            else:
                parent[x] = y
                ms[y] += 1
        
        for v1, v2 in edges:
            union(v1, v2)

        return len(set([find(i) for i in range(n)]))
