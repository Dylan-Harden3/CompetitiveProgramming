class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        res = []

        visited = [0] * numCourses
        def dfs(course):
            visited[course] = 1
            for nei in adj[course]:
                if visited[nei] == 1:
                    return True
                elif visited[nei] == 0 and dfs(nei):
                    return True
            visited[course] = 2
            res.append(course)
            return False
        for course in range(numCourses):
            if visited[course] == 0 and dfs(course): return []
        return res
