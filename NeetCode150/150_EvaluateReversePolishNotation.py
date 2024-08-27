class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = set(['+', '-', '*', '/'])
        for c in tokens:
            if c == '+':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1+n2)
            elif c == '-':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1-n2)
            elif c == '/':
                n2 = stack.pop()
                n1 = stack.pop()
                if n1 * n2 > 0:
                    stack.append(n1//n2)
                else:
                    stack.append(ceil(n1/n2))
            elif c == '*':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1*n2)
            else:
                stack.append(int(c))
            if c in s:
                print(stack[-1])
        return stack[-1]
