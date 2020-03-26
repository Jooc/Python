class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack:
                    return False
                if match[stack.pop()] != c:
                    return False

        return len(stack) == 0


demo = Solution()
print(demo.isValid("]"))
