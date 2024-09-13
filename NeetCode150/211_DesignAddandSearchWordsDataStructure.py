class TrieNode:
    def __init__(self):
        self.nei = {}
        self.isEOW = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.nei:
                cur.nei[c] = TrieNode()
            cur = cur.nei[c]
        cur.isEOW = True

    def helper(self, node, word):
        for i, c in enumerate(word):
            if c == '.':
                for t in node.nei:
                    if self.helper(node.nei[t], word[i+1:]):
                        return True
                return False
            else:
                if c not in node.nei:
                    return False
                node = node.nei[c]
        return node.isEOW
    def search(self, word: str) -> bool:
        return self.helper(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
