class Solution:
    def reverse(self, x):
        ans = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        return ans if -(2 ** 31) <= ans <= 2 ** 31 else 0


demo = Solution()
print(demo.reverse(123456789101111))

# class Solution:
#     def reverse(self, x):
#         ans = 0
#         minus = False
#
#         if x < 0:
#             minus = True
#             x = -x
#
#         while x != 0:
#             pop = x % 10
#             x = x // 10
#
#             temp = ans * 10 + pop
#             ans = temp
#
#         if not -2**31 <= ans <= 2**31 - 1:
#             return 0
#
#         return -ans if minus else ans
