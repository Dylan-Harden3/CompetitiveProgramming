
class TrieNode:
    def __init__(self,val=''):
        self.children = dict()
        self.is_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M, N = len(board), len(board[0])
        res = set()

        prefix = []
        visit = set()
        def search(row, col, node, word):
            if (
                min(row, col) < 0
                or row == M
                or col == N
                or board[row][col] not in node.children
                or (row, col) in visit
            ):
                return
            
            visit.add((row, col))
            word += board[row][col]
            node = node.children[board[row][col]]
            
            if node.is_word:
                res.add(word)

            search(row+1, col, node, word)
            search(row-1, col, node, word)
            search(row, col+1, node, word)
            search(row, col-1, node, word)

            visit.remove((row, col))

        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        for i in range(M):
            for j in range(N):
                search(i, j, trie.root, "")
        return list(res)
