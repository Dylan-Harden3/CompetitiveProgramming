class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = set(['{', '(', '['])
        closes = set(['}', ')', ']'])

        m = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }
        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if not stack or m[stack[-1]] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0
