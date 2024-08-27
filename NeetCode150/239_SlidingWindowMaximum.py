class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])

        for i in range(k, len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            while i-k >= q[0]:
                q.popleft()
            res.append(nums[q[0]])
        
        return res
