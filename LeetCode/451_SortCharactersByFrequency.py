class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        counts = Counter(s)
        freqs = defaultdict(list)

        for c, n in counts.items():
            freqs[n].append(c)

        for i in range(len(s), 0, -1):
            for c in freqs[i]:
                res.append(c * i)

        return "".join(res)
