class Node:
    def __init__(self):
        self.neighbors = {}
        self.isEOW = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.neighbors:
                cur.neighbors[c] = Node()
            cur = cur.neighbors[c]
        cur.isEOW = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.neighbors:
                return False
            cur = cur.neighbors[c]
        return cur.isEOW

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.neighbors:
                return False
            cur = cur.neighbors[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
