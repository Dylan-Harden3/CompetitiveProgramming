class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            n = int(s[start:i])
            i += 1
            strs.append(s[i:i+n])
            i = i+n
        return strs