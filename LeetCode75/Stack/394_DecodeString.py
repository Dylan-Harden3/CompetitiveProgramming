class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ""

        for c in s:
            if c == "]":
                cur = ""
                while stack and stack[-1] != '[':
                    cur = stack.pop() + cur
                stack.pop()

                power = 0
                count = 0
                while stack and stack[-1].isdigit():
                    count += int(stack[-1]) * pow(10, power)
                    power += 1
                    stack.pop()
                stack.append(cur * count)
            else:
                stack.append(c)

        return "".join(stack)
