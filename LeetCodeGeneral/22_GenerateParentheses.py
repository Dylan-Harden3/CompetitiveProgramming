class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        sols = set()
        def backtrack(opened, closed):
            if opened == closed and closed == n:
                sols.add(''.join(stack))
                return
            
            if closed > opened:
                return

            if opened < n:
                stack.append('(')
                backtrack(opened + 1, closed)
                stack.pop()
            
            stack.append(')')
            backtrack(opened, closed + 1)
            stack.pop()

        backtrack(0, 0)
        return list(sols)
