s = "1a2"


class Solution(object):
    def __init__(self):
        pass

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.ascii_check(s[l]):
                l += 1
            while r > l and not self.ascii_check(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def ascii_check(self, x):

        return ((ord('A') <= ord(x) <= ord('Z')) or
                (ord('a') <= ord(x) <= ord('z')) or
                (ord('0') <= ord(x) <= ord('9')))


output = Solution()
print(output.isPalindrome(s))
