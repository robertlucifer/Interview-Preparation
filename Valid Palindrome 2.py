s = "1a2"


class Solution(object):
    def __init__(self):
        pass

    def isPalindrome(self, s: str) -> bool:
        result = ""

        for x in s:
            if x.isalnum():
                result += x
        return result.lower() == result[::-1].lower()


output = Solution()
print(output.isPalindrome(s))
