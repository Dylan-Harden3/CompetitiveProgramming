class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]

        pairs = sorted(pairs, key=lambda n: n[1], reverse=True)
        heap = pairs[:k]
        heapq.heapify(heap)
        cur_sum = sum([p[0] for p in heap])
        sol = cur_sum * min([p[1] for p in heap])

        for i in range(k, len(nums1)):
            min_el = pairs[i][1]

            cur_sum -= heapq.heappop(heap)[0]
            cur_sum += pairs[i][0]
            sol = max(sol, min_el * cur_sum)

            heapq.heappush(heap, pairs[i])
        return sol
