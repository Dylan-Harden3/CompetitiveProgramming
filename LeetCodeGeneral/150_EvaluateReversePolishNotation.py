class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set()
        ops.add('+')
        ops.add('-')
        ops.add('*')
        ops.add('/')
        for token in tokens:
            if token in ops:
                v2 = stack.pop()
                v1 = stack.pop()
    
            if token == '+':
                stack.append(v1 + v2)
            elif token == '-':
                stack.append(v1 - v2)
            elif token == '*':
                stack.append(v1 * v2)
            elif token == '/':
                stack.append(math.floor(v1 / v2) if v1*v2 > 0 else math.ceil(v1 / v2))
            else:
                stack.append(int(token))
            # print(stack)
        return stack[0]
