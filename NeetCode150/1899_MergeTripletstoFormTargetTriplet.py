class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = []
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                candidates.append([a, b, c])
        found = [False, False, False]
        for a, b, c in candidates:
            if a == target[0]:
                found[0] = True
            if b == target[1]:
                found[1] = True
            if c == target[2]:
                found[2] = True

        return False not in found
