class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapify(stones)

        while len(stones) > 1:
            s1 = -heappop(stones)
            s2 = -heappop(stones)

            if s1 != s2:
                heappush(stones, -(s1 - s2))

        return -stones[0] if stones else 0
