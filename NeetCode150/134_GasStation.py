class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for i in range(len(gas)):
            gas[i] = gas[i] - cost[i]

        res = -1
        tank = 0
        cur = 0
        for i in range(len(gas)):
            if gas[i] >= 0 and cur <= 0:
                cur = 0
                res = i
            
            cur += gas[i]
            if cur < 0:
                res = -1
            tank += gas[i]

        return res if tank >= 0 else -1
