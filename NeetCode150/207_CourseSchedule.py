class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)

        visit = defaultdict(int)
        def cycleCheck(course):
            visit[course] = 1

            for nei in adj[course]:
                if visit[nei] == 1:
                    return True
                elif visit[nei] == 0 and cycleCheck(nei):
                    return True
            
            visit[course] = 2
            return False

        for course in range(numCourses):
            if cycleCheck(course):
                return False
        
        return True
