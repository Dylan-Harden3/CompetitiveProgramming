class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        parent = [i for i in range(len(nums))]
        ms = [1] * len(nums)
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
                ms[x] += ms[y]
            elif ms[x] < ms[y]:
                parent[x] = y
                ms[y] += ms[x]
            else:
                parent[x] = y
                ms[y] += ms[x]
        
        factorIdx = {}
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factorIdx:
                        union(i, factorIdx[f])
                    else:
                        factorIdx[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factorIdx:
                    union(i, factorIdx[n])
                else:
                    factorIdx[n] = i
        for i in range(len(nums)):
            if i == 0:
                leader = find(i)
            elif find(i) != leader:
                return False
        return True
