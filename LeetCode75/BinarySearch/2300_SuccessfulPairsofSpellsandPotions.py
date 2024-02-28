class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        N, M = len(spells), len(potions)

        potions.sort()

        pairs = [0] * N
        for i, spell in enumerate(spells):
            l, r = 0, M-1
            minPotion = M
            while l <= r:
                m = (l + r) // 2
                if spell * potions[m] >= success:
                    r = m-1
                    minPotion = m
                else:
                    l = m+1
            pairs[i] += M - minPotion
        return pairs
