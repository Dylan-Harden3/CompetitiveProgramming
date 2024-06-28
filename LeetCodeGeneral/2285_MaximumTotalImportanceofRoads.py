class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counts = [0] * n

        for v1, v2 in roads:
            counts[v1] += 1
            counts[v2] += 1
        
        new_counts = [(c, i) for i, c in enumerate(counts)]
        new_counts.sort(key=lambda x: x[0], reverse=True)

        labels = [0] * n
        for _, v in new_counts:
            labels[v] = n
            n -= 1
        
        imp = 0
        for v1, v2 in roads:
            imp += labels[v1] + labels[v2]

        return imp