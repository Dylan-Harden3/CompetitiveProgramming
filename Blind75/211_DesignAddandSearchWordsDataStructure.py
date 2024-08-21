class Trie:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_word = True
    
    def helper(self, node, word):
        for i, c in enumerate(word):
            if c == ".":
                for candidate in node.children:
                    if self.helper(node.children[candidate], word[i+1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.is_word

    def search(self, word: str) -> bool:
        return self.helper(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
