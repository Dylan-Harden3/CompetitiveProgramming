class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = 0
        for i2 in range(l2):
            cur = [] if i2 == 0 else [0] * i2
            carry = 0
            for i1 in range(l1):
                base = int(num1[i1]) * int(num2[i2]) + carry
                carry = base // 10
                cur.append(base % 10)
            if carry > 0:
                cur.append(carry)
            for i, n in enumerate(cur):
                res += (10**i)*n
        return str(res)
