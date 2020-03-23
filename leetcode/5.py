def longestPalindrome(s: str) -> str:
    size = len(s)
    if size < 2:
        return s

    dp = [[False for _ in range(size)] for _ in range(size)]

    for i in range(size):
        dp[i][i] = True

    for j in range(1, size):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i + 1 < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

    for row in dp:
        print(row)

    max_len = 1
    max_str = s[0]
    for j in range(1, size):
        for i in range(0, j):
            if dp[i][j]:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_str = s[i:j+1]

    return max_str


print(longestPalindrome('ab'))