def coinChange(coins: list, amount: int) -> int:
    dp = list()
    for _ in range(amount + 1):
        dp.append(float('INF'))

    dp[0] = 0
    for index in range(1, amount + 1):
        for coin in coins:
            if index - coin < 0:
                continue
            dp[index] = min(dp[index], 1 + dp[index - coin])

    return dp[amount] if dp[amount] != float('INF') else -1


print(coinChange([2], 3))

# def coinChange(coins: list, amount: int) -> int:
#     if amount == 0: return -1
#
#     memo = dict()
#
#     def dp(n):
#         if n in memo:
#             return memo[n]
#
#         if n == 0:
#             return 0
#         if n < 0:
#             return -1
#
#         res = float('INF')
#         for coin in coins:
#             sub = dp(n - coin)
#             if sub == -1:
#                 continue
#             res = min(res, sub + 1)
#
#         memo[n] = res if res != float('INF') else -1
#
#         print(memo)
#         return memo[n]
#
#     return dp(amount)


