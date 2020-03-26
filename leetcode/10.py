class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    firstMatch = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or firstMatch and dp(i + 1, j)
                    else:
                        ans = firstMatch and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


demo = Solution()
print(demo.isMatch("ab", ".*c"))
