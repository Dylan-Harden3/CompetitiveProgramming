class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            cur = i
            while s[cur].isdigit():
                cur += 1
            n = int(s[i:cur])
            cur += 1
            res.append(s[cur:cur+n])
            i = cur+n
        return res
