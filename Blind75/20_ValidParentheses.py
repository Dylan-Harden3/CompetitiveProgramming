class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = set(['[', '(', '{'])
        closes = set([']', ')', '}'])

        d = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if len(stack) == 0:
                    return False
                if d[c] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0