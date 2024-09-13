class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        sol = []
        stack = []
        def backtrack(i):
            if i == len(s):
                sol.append(stack.copy())
                return
            for j in range(i+1, len(s)+1):
                if is_palindrome(s[i:j]):
                    stack.append(s[i:j])
                    backtrack(j)
                    stack.pop()
        backtrack(0)
        return sol
