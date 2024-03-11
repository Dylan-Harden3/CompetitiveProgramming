class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        col = [-1] * len(graph)
        for u in range(len(graph)):
            if col[u] != -1:
                continue
            stack = [(u, 0)]

            while stack:
                cur, color = stack.pop()
                if col[cur] == -1:
                    col[cur] = color
                    for nei in graph[cur]:
                        stack.append((nei, (color+1) % 2))
                if col[cur] != color:
                    return False

        return True