class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []

        for num, count in Counter(arr).items():
            heap.append((count, num))

        heapq.heapify(heap)

        for i in range(k):
            count, num = heapq.heappop(heap)
            if count > 1:
                count -= 1
                heapq.heappush(heap, (count, num))

        return len(heap)
