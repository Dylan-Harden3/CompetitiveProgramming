class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        sol = ''

        def divides(substr, s):
            if len(substr) > len(s) or len(s) % len(substr) != 0:
                return False

            return substr * (len(s) // len(substr)) == s

        for i in range(1, len(str1)+1):
            if divides(str1[:i], str1) and divides(str1[:i], str2) and len(str1[:i]) > len(sol):
                sol = str1[:i]

        return sol
