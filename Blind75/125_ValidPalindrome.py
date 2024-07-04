class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        c = []
        for el in s:
            if el.isalnum():
                c.append(el)

        s = ''.join(c)
        for i in range(len(s) // 2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True