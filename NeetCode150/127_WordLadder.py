class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i] + '*' + word[i+1:]].append(word)
        
        visit = set()
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):
                    candidate = cur[:j] + '*' + cur[j+1:]
                    for nextWord in adj[candidate]:
                        if nextWord not in visit:
                            visit.add(nextWord)
                            q.append(nextWord)
            res += 1
        
        return 0
