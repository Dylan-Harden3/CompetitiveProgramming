class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        res = []
        counter = 0
        while i < len(word1) and j < len(word2):
            res.append(word1[i] if counter % 2 == 0 else word2[j])
            if counter % 2 == 0:
                i += 1
            else:
                j += 1
            counter += 1

        while i < len(word1):
            res.append(word1[i])
            i += 1
        
        while j < len(word2):
            res.append(word2[j])
            j += 1

        return "".join(res)
