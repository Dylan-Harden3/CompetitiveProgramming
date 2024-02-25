class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y:
            return
        
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
    
    def numSets(self):
        leaders = set()
        for i in range(len(self.parent)):
            l = self.find(i)
            if l not in leaders:
                leaders.add(l)

        return len(leaders)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)

        for i in range(N):
            for j in range(N):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        return uf.numSets()
