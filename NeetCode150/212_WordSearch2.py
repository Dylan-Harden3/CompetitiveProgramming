class TrieNode:
    def __init__(self):
        self.isEOW = False
        self.nei = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.nei:
                cur.nei[c] = TrieNode()
            cur = cur.nei[c]
        cur.isEOW = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        sols = set()
        visit = set()
        def search(i, j, node, word):
            if node.isEOW:
                sols.add(word)
            if min(i, j) < 0 or i == len(board) or j == len(board[0]) or board[i][j] not in node.nei or (i, j) in visit:
                return
            
            visit.add((i, j))
            word += board[i][j]
            search(i+1, j, node.nei[board[i][j]], word)
            search(i-1, j, node.nei[board[i][j]], word)
            search(i, j-1, node.nei[board[i][j]], word)
            search(i, j+1, node.nei[board[i][j]], word)
            visit.remove((i, j))

        for word in words:
            trie.add(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, trie.root, "")
        
        return list(sols)

