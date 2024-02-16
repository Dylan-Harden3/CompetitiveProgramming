class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = [c for c in senate]
        d = deque()
        r = deque()

        for i, c in enumerate(senate):
            if c == 'D':
                d.appendleft(i)
            elif c == 'R':
                r.appendleft(i)

        while d and r:
            dSen, rSen = d.pop(), r.pop()

            if dSen < rSen:
                d.appendleft(rSen + len(senate))
            else:
                r.appendleft(dSen + len(senate))
        
        return "Radiant" if r else "Dire"
