class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]

        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n - 1]


demo = Solution()
print(demo.climbStairs(16))





# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {1: 1, 2: 2}
#
#         def up(n):
#             if n in memo:
#                 return memo[n]
#
#             if n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
#
#             else:
#                 memo[n] = up(n - 1) + up(n - 2)
#                 return memo[n]
#
#         return up(n)
#
#
# demo = Solution()
# print(demo.climbStairs(16))
