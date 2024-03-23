class Solution:
    def calculate(self, s: str) -> int:

        cur = res = i = 0
        sign = 1
        stack = []

        while i < len(s):
            c = s[i]
            if c.isdigit():
                cur = cur*10 + int(c)
            elif c in ['+', '-']:
                res += sign * cur
                sign = 1 if c == '+' else -1
                cur = 0
            elif c == '(':
                stack.append((res, sign))
                sign = 1
                res = 0
            elif c == ')':
                prev, prevsign = stack.pop()
                res += cur*sign
                res *= prevsign
                res += prev
                cur = 0
            i += 1
        return res + sign * cur
