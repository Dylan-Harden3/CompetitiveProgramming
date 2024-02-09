class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        res = []

        for word in words:
            if word:
                res.append(word)

        return ' '.join(res[::-1])
