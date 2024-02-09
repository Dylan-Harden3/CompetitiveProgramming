class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

        sVowels = []

        for i, c in enumerate(s):
            if c in vowels:
                sVowels.append(c)

        idx = len(sVowels)-1
        res = []
        for i in range(len(s)):
            if s[i] in vowels:
                res.append(sVowels[idx])
                idx -= 1
            else:
                res.append(s[i])

        return ''.join(res)
