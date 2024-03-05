class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [c for c in s if c.isalnum()]
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
