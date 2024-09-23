class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for dst, src in prerequisites:
            adj[src].append(dst)
        
        res = []
        visit = defaultdict(int)
        def cycleCheck(course):
            visit[course] = 1

            for nei in adj[course]:
                if visit[nei] == 1:
                    return True
                elif visit[nei] == 0 and cycleCheck(nei):
                    return True
            
            visit[course] = 2
            res.append(course)
            return False
        
        for course in range(numCourses):
            if visit[course] == 0 and cycleCheck(course):
                return []
        return res[::-1]
