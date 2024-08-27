class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x : x[0], reverse=True)

        stack = deque()
        for pos, speed in cars:
            stack.append((pos, speed, (target-pos)/speed))
        # print(stack)
        res = 0  
        while stack:
            cur_end = stack[0][2]
            stack.popleft()

            while stack and stack[0][2] <= cur_end:
                stack.popleft()
            
            res += 1

        return res
