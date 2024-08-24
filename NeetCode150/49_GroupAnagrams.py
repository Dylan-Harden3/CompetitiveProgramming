class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            x = list(s)
            x.sort()
            anagrams[''.join(x)].append(s)

        return list(anagrams.values())
