class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        meetingsHeld = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                meetingsHeld[room] += 1
                heapq.heappush(used, (end, room))
            else:
                nearestEnd, room = heapq.heappop(used)
                meetingsHeld[room] += 1
                heapq.heappush(used, (nearestEnd + (end - start), room))
        
        return meetingsHeld.index(max(meetingsHeld))
