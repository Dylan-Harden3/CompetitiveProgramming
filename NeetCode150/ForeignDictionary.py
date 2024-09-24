class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)

        for w1, w2 in zip(words, words[1:]):
            minl = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minl] == w2[:minl]:
                return ''
            for i in range(minl):
                if w1[i] != w2[i]:
                    adj[w1[i]].append(w2[i])
                    break
        
        visit = defaultdict(int)
        res = []
        def dfs(c):
            visit[c] = 1
            for nei in adj[c]:
                if visit[nei] == 1:
                    return False
                elif visit[nei] == 0 and not dfs(nei):
                    return False
            visit[c] = 2
            if c not in res:
                res.append(c)
            return True
        for i in range(len(words)):
            for j in range(len(words[i])):
                if not dfs(words[i][j]):
                    return ''
        return ''.join(res[::-1])
