class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        o = set(['(', '{', '['])
        c = set([')', '}', ']'])
        m  = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for t in s:
            if t in o:
                stack.append(t)
            else:
                if stack and m[t] != stack[-1] or not stack:
                    return False
                
                stack.pop()
        return len(stack) == 0
