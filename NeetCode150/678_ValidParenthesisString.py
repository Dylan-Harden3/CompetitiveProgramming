class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen, maxOpen = 0, 0

        for c in s:
            if c == ')':
                minOpen -= 1
                maxOpen -= 1
            elif c == '(':
                minOpen += 1
                maxOpen += 1
            elif c == '*':
                minOpen -= 1
                maxOpen += 1
            if maxOpen < 0:
                return False
            if minOpen < 0:
                minOpen = 0
        return minOpen == 0
