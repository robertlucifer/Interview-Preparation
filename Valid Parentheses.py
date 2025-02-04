class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for x in s:
            if x in brackets:
                if stack and stack[-1] == brackets[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False
obj=Solution()
strs="([])"
output = obj.isValid(strs)
print(output)
