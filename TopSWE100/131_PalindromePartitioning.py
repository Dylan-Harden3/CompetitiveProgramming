class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            if len(s) == 0:
                return False
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True

        
        res = []
        stack = []

        def backtrack(i):
            if i == len(s):
                res.append(stack.copy())
                return

            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    stack.append(s[i:j])
                    backtrack(j)
                    stack.pop()

        backtrack(0)
        return res
