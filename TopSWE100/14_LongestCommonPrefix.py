class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min([len(s) for s in strs])
        for i, s in enumerate(strs):
            if len(s) == l:
                shortest = s
                break

        prefix = []
        for i in range(l):
            flag = True
            for j in range(len(strs)):
                if strs[j][i] != shortest[i]:
                    flag = False
                    break
            if flag:
                prefix.append(shortest[i])
            else:
                break
        return "".join(prefix)
