def superEggDrop(K: int, N: int) -> int:

    # dp状态定义
    # dp[k][m] = n
    # 有k个鸡蛋，最多扔m次，可以解出n层楼的问题
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

    m = 0

    while dp[K][m] < N:
        m += 1
        for k in range(1, K + 1):
            dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1

    return m


print(superEggDrop(2,6))








# Advanced DP
# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         memo = {}
#
#         def dp(K, N) -> int:
#             if K == 1:
#                 return N
#             if N == 0:
#                 return 0
#
#             if (K, N) in memo:
#                 return memo[(K, N)]
#
#             res = float('inf')
#             low, high = 1, N
#             while low <= high:
#                 mid = (low + high) // 2
#                 broke = dp(K - 1, mid - 1)
#                 not_broke = dp(K, N - mid)
#                 if broke > not_broke:
#                     high = mid - 1
#                     res = min(res, broke + 1)
#                 else:
#                     low = mid - 1
#                     res = min(res, not_broke + 1)
#
#             memo[(K, N)] = res
#             return memo[(K, N)]
#
#         return dp(K, N)
#
#
# demo = Solution()
# print(demo.superEggDrop(4, 2000))
# print(demo.memo)



# 暴力dp
# class Solution:
#     def __init__(self):
#         self.memo = dict()
#
#     def superEggDrop(self, K: int, N: int) -> int:
#         def dp(K, N) -> int:
#             if K == 1: return N
#             if N == 0: return 0
#
#             if (K, N) in self.memo:
#                 return self.memo[(K, N)]
#
#             res = float('INF')
#
#             for i in range(1, N + 1):
#                 res = min(res, max(dp(K - 1, i - 1), dp(K, N - i)) + 1)
#
#             self.memo[(K, N)] = res
#             return self.memo[(K, N)]
#
#         return dp(K, N)

