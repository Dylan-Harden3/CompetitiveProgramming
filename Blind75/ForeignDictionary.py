class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            if (
                len(word1) > len(word2)
                and word1[:len(word2)] == word2
            ):
                return ''
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visit = {}
        res = []
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True
            res.append(node)
            visit[node] = False

        for c in adj:
            if dfs(c):
                return ''
        
        return ''.join(res[::-1])
