class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = []
        for k, v in Counter(word).items():
            counts.append((k, v))

        counts.sort(key=lambda x: x[1], reverse=True)
        res = 0
        chars = 0
        for _, count in counts:
            chars += 1
            res += (count) * (ceil(chars / 8))
        return res