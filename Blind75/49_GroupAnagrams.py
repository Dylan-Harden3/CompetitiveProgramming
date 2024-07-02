class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bag = defaultdict(list)
        for s in strs:
            bag[''.join(sorted(s))].append(s)
        return [v for v in bag.values()]