class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        l, r = candidates, n-candidates-1

        left = zip(range(l), [0]*l)
        right = zip(range(max(l, r+1), n), [1]*(n - max(l, r+1)))

        heap = [(costs[idx], side) for idx, side in chain(left, right)]
        heapq.heapify(heap)

        res = 0
        for _ in range(k):
            cost, side = heapq.heappop(heap)
            res += cost

            if l > r: continue

            if side == 0:
                heapq.heappush(heap, (costs[l], 0))
                l += 1
            else:
                heapq.heappush(heap, (costs[r], 1))
                r -= 1
        return res
