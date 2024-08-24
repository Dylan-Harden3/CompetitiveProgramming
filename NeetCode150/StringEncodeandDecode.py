class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append('#')
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # skip '#'
            i += 1
            j = i
            while s[j].isdigit():
                j += 1
            strlen = int(s[i:j])
            j += 1
            res.append(s[j:j+strlen])
            i = j + strlen

        return res
