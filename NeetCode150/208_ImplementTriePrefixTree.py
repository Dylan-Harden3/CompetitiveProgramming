class TrieNode:
    def __init__(self):
        self.nei = {}
        self.isEOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.nei:
                cur.nei[c] = TrieNode()
            cur = cur.nei[c]
        cur.isEOW = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.nei:
                return False
            cur = cur.nei[c]
        return cur.isEOW

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.nei:
                return False
            cur = cur.nei[c]
        return True  


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
