class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        visit = set()
        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            elif src not in adj:
                return False
            
            temp = list(adj[src])
            for i, nei in enumerate(temp):
                res.append(nei)
                adj[src].pop(i)
                if dfs(nei):
                    return True
                adj[src].insert(i, nei)
                res.pop()
            return False
        dfs('JFK')
        return res

            
